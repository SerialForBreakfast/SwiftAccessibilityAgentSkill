#!/bin/sh
# Check path categories against Git itself, including already tracked files.
set -eu
cd "$(git rev-parse --show-toplevel)"
for path in evals/results/private/report.json deliveries/discovery-500-v1-return.zip \
    deliveries/request-1507-continuation-return.zip tool/.env.local client.key \
    certs/client.pem scratch/first.xcresult/Info.plist tests/__pycache__/test.pyc; do
    git check-ignore --no-index -q "$path" || { echo "Not protected: $path" >&2; exit 1; }
done
for path in evals/.env.example evals/discovery-500/subjects.zip \
    evals/discovery-500/controller.json evals/discovery-500/GRADING.md; do
    if git check-ignore --no-index -q "$path"; then echo "Incorrectly hidden: $path" >&2; exit 1; fi
done
tracked=$(git ls-files -ci --exclude-standard)
[ -z "$tracked" ] || { printf 'Tracked despite ignore rules:\n%s\n' "$tracked" >&2; exit 1; }
