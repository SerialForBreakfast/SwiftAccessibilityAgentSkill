#!/bin/sh
# Check path categories against Git itself, including already tracked files.
set -eu
cd "$(git rev-parse --show-toplevel)"
for path in evals/results/private/report.json deliveries/discovery-500-v1-return.zip \
    deliveries/request-1507-continuation-return.zip tool/.env.local client.key \
    certs/client.pem scratch/first.xcresult/Info.plist tests/__pycache__/test.pyc \
    evals/proof-repair-20/replay/answer.txt evals/proof-repair-20/subject-only.zip \
    evals/proof-repair-20/return-receipt.json evals/proof-repair-20/working/first.log; do
    git check-ignore --no-index -q "$path" || { echo "Not protected: $path" >&2; exit 1; }
done
for path in evals/.env.example evals/discovery-500/subjects.zip \
    evals/discovery-500/controller.json evals/discovery-500/GRADING.md \
    evals/proof-repair-20/evidence.json evals/proof-repair-20/replay/RESULTS.md \
    evals/rc2-starter-comparison/results/README.md; do
    if git check-ignore --no-index -q "$path"; then echo "Incorrectly hidden: $path" >&2; exit 1; fi
done
tracked=$(git ls-files -ci --exclude-standard)
[ -z "$tracked" ] || { printf 'Tracked despite ignore rules:\n%s\n' "$tracked" >&2; exit 1; }
