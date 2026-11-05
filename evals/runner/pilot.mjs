/** Offline bounded pilot manifest. No transport or model execution. */
import { pathToFileURL } from 'node:url';
import { planCampaign } from './campaign.mjs';
import { hash } from './lib.mjs';

export function planPilot(worker) {
  const campaign = planCampaign({ worker, profile: 'compact', split: 'development' });
  // OS pairing is intentional only for the version-sensitive family in this pilot.
  const families = ['D01', 'D02', 'D03', 'D31', 'D33', 'D36', 'D38'];
  const jobs = campaign.jobs.filter(j => families.includes(j.family) && j.repeat === 0 &&
    (j.family === 'D38' || j.os === '26'));
  const minimumGenerationRequests = jobs.reduce((n, j) => n + j.userTurns.length, 0);
  const { planHash, ...base } = campaign;
  const body = {
    ...base, campaignPlanHash: planHash, experiment: 'bounded-worker-pilot-v1',
    purpose: 'Capability qualification and descriptive development comparison; not release acceptance.',
    scope: { families, repetitions: 1, heldout: false, freeRunningHistory: true },
    limits: {
      concurrency: 1, maximumJobs: jobs.length, minimumGenerationRequests,
      maximumGenerationRequests: 200, wallClockMinutes: 45, requestTimeoutSeconds: 120,
      automaticRetries: 0, paidCalls: 0, maximumNewModelDownloads: 0,
      onLimit: 'Stop and return cancelled receipts for unstarted jobs; retain partial and unknown outcomes.'
    },
    qualification: 'Worker must confirm pinned model/runtime/template, exact token fit, available memory, and ability to enforce every limit before execution. Otherwise return blocked; never silently substitute.',
    jobs
  };
  return { ...body, planHash: hash(JSON.stringify(body)) };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const [worker, ...extra] = process.argv.slice(2);
  if (!['bigdog', 'maxmini'].includes(worker) || extra.length) {
    throw Error('Usage: node evals/runner/pilot.mjs bigdog|maxmini');
  }
  process.stdout.write(JSON.stringify(planPilot(worker), null, 2) + '\n');
}
