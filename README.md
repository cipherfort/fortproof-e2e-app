# attestra-e2e-app

Throwaway sample application for the [Attestra](https://github.com/cipherfort/attestra) end-to-end test.

`requirements.txt` pins **PyYAML 5.3 on purpose**: it has known critical vulnerabilities (e.g. CVE-2020-14343), so
the platform's vulnerability feeds should raise a finding, and upgrading it should close the finding. Do not use this
code for anything else. Safe to delete.
