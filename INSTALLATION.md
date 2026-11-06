# Installation and Upgrades

[Back to project overview](README.md)

## Install As a Skill

Most users should install this skill from the root of the project where they want their agent to use it.

Example:

```bash
cd /path/to/your/project
```

If you install it there, the skill is available to that project without affecting every other project on your machine.

### Before You Start

You need:
- Terminal access on macOS
- A current Node.js LTS installation (`node` and `npx`); the skills CLI currently requires Node.js 22.20 or later
- Git available (`git`)
- Internet access to download the skill

Quick check:

```bash
git --version
node --version
npx --version
```

If all commands print a version number, continue to the install step.

Homebrew is optional. You can install the official [Node.js LTS package](https://nodejs.org/en/download) directly. The [skills CLI documentation](https://github.com/vercel-labs/skills) describes prerequisites and agent selection.

### If You Do Not Have Homebrew

Homebrew is the easiest way for many macOS users to install Node.js.

Official Homebrew install command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After Homebrew finishes, open a new Terminal window or follow the PATH instructions it prints.

### Install Node.js

Recommended on macOS if you use Homebrew:

```bash
brew install node
```

If you do not want to use Homebrew, install the official Node.js LTS package from:

- [nodejs.org/download](https://nodejs.org/en/download)

Then confirm Node.js is available:

```bash
node --version
npx --version
```

### Install in Your Project Directory

From the root of the app or repository where you want the skill available:

```bash
npx skills add https://github.com/SerialForBreakfast/SwiftAccessibilityAgentSkill --skill swift-accessibility-agent
```

The installer lets you select your coding agent(s). Project-local is the default;
no particular LLM vendor is required. Read its destination summary before accepting.
For automation, select a supported agent explicitly, for example `--agent codex --yes`.
See the [agent/path reference](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

### Verify Installation

First, confirm the CLI sees the skill:

```bash
npx skills list
```

For the shared `.agents` layout, confirm the entry file below. For other layouts,
use the path printed by the installer. This check also follows a symlink:

```bash
test -f .agents/skills/swift-accessibility-agent/SKILL.md && echo "Skill entry found"
```

For Codex and other agents using the shared `.agents` layout, the project-local path is:

```text
./.agents/skills/swift-accessibility-agent/SKILL.md
```

If the skill installs correctly but does not appear in the active session immediately, refresh or restart the session.

### What New Users Should Do

1. Open Terminal.
2. `cd` into the project you are actively working on.
3. Make sure `node` and `npx` work.
4. Run the install command once.
5. Verify the skill appears in `npx skills list`.
6. Start or refresh your agent session in that project.

### Optional: Global Install Alternative

Use this only if you want the skill available across multiple projects instead of just one:

```bash
npx skills add https://github.com/SerialForBreakfast/SwiftAccessibilityAgentSkill --skill swift-accessibility-agent --agent codex --global --yes
```

Global destinations depend on the selected agent. The current CLI documents
`~/.agents/skills/` for Codex; use the installer summary and
`npx skills list --global` to check your actual destination.

## Upgrade

There are two common upgrade paths.

### Upgrade With `npx skills add`

If you installed the skill through the normal skills workflow, go to the project where you installed it and run the install command again:

```bash
cd /path/to/your/project
npx skills add https://github.com/SerialForBreakfast/SwiftAccessibilityAgentSkill --skill swift-accessibility-agent
```

Then verify:

```bash
npx skills list
test -f .agents/skills/swift-accessibility-agent/SKILL.md && echo "Skill entry found"
```

This is the safest default upgrade path for most users.

### Upgrade a Local Clone With `git status --short
git pull origin main`

If you keep a local clone of this repository and use it directly, update the repo first:

```bash
cd /path/to/SwiftAccessibilityAgent
git pull origin main
```

Preserve any local edits before pulling. Resolve conflicts explicitly rather than
overwriting your changes. Updating a clone does not update a separately copied skill.

After pulling:

- if you use the skills install workflow, re-run `npx skills add ...` from the target project
- if you use Xcode compatibility linking, re-run `./scripts/install-for-xcode.sh` or recreate the manual symlink

### Manual Upgrade Checklist

1. Update the repo or re-run the install command.
2. Confirm the version in `SKILL.md` or `VERSION`.
3. Restart the active Codex or Xcode session if it was already open.
4. Re-test one known prompt, such as `Tell me about UILabel accessibility.`

## Use With Xcode

Apple documents agent plugins and invokable skills in Xcode 27. The compatibility link below is the repository's existing setup; a symlink alone does not establish discovery in every Xcode/agent version. Confirm the skill is actually selected before relying on it. Keep `npx skills` as the primary installation route. See the [reviewed host-capability notes](docs/core/apple-beta-release-readiness-2026.md).

`npx skills add ...` remains the first-class install path for this repository.

If you also want to use the same skill content with Xcode's Codex agent, install an Xcode compatibility link from this repository root:

```bash
./scripts/install-for-xcode.sh
```

What this does:
- creates Xcode's Codex customization directory if needed
- creates a symlink from Xcode's Codex directory to this repository
- keeps `SKILL.md`, `agents/openai.yaml`, and `references/` as the single source of truth

Expected Xcode compatibility path:

```text
~/Library/Developer/Xcode/CodingAssistant/codex/swift-accessibility-agent
```

Verify the link:

```bash
ls -la ~/Library/Developer/Xcode/CodingAssistant/codex/swift-accessibility-agent
```

If Xcode is already open, quit and reopen it after running the script.

### Manual Xcode Install

If you do not want to run the helper script, you can create the Xcode compatibility link manually.

From this repository root:

```bash
mkdir -p ~/Library/Developer/Xcode/CodingAssistant/codex
ln -s "$(pwd)" ~/Library/Developer/Xcode/CodingAssistant/codex/swift-accessibility-agent
```

Then verify:

```bash
ls -la ~/Library/Developer/Xcode/CodingAssistant/codex/swift-accessibility-agent
```

Expected entry files:

```text
~/Library/Developer/Xcode/CodingAssistant/codex/swift-accessibility-agent/SKILL.md
~/Library/Developer/Xcode/CodingAssistant/codex/swift-accessibility-agent/agents/openai.yaml
```

If Xcode is already open, quit and reopen it after creating the link.

### Recommended Xcode Workflow

If the manual link command reports an existing destination, inspect it with `ls -la`
before making changes. The command intentionally does not replace an existing file
or link. Review the helper script before running it; its replacement behavior differs.

1. Keep the main install path as `npx skills add ...` for Codex/skills-based workflows.
2. From this repository root, either run `./scripts/install-for-xcode.sh` or create the link manually.
3. Restart Xcode.
4. Open your project in Xcode and use the Codex agent there.

### Troubleshooting

If `node` or `npx` is not found:
- Install Node.js first, then reopen Terminal.

If `brew` is not found:
- Install Homebrew first, or install Node.js directly from [nodejs.org/download](https://nodejs.org/en/download).

If `git` is not found:
- Install Apple's Command Line Tools when macOS prompts you, then reopen Terminal.

If the install command works but the skill does not appear in your session:
- Refresh or restart the session in the same project directory.

If you accidentally installed globally but wanted project-local behavior:
- Go back to your project directory and run the project-local install command there.

If Xcode does not pick up the compatibility install:
- Confirm `~/Library/Developer/Xcode/CodingAssistant/codex/swift-accessibility-agent/SKILL.md` exists.
- Quit and reopen Xcode.
- Re-run `./scripts/install-for-xcode.sh` from this repository root.


## Installed Skill Checklist

- `SKILL.md` exists at the installed root.
- `agents/openai.yaml` and referenced guidance are present.
- Start a fresh session and ask an accessibility question.
- Confirm the skill was selected and its cited references are accessible.

Evaluation and native unit-test dependencies are separate from skill installation.
See [the companion library](code-examples/README.md) for contributor tooling.
