# Ordinary controls and optional shortcuts

Keep visible/ordinary operations alongside rotor/custom-action shortcuts. Route each operation to its intended current item without removing swipe, drag, keyboard or button paths supplied by the task. Disabled native controls must also reject programmatic callback dispatch where the component contract requires it. Rebinding must replace owned handlers, not accumulate them. Test the actual native entry point: a stale AppKit selector can create a fresh closure and bypass an otherwise correct captured-generation guard.

Use only for this concern. Apply Apple source/SDK contracts to the actual target; examples and application policies are not universal platform guarantees.

When disabled, both ordinary and shortcut paths must honor the intended policy. Reconfiguring the same instance must replace or detach obsolete handlers; do not hide visible buttons merely to simplify grouping.
