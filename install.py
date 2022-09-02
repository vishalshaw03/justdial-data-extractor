import sys
import subprocess
import pkg_resources

# necessary packages
names = {"requests", "html5lib", "bs4"}


class CheckPackage:
    def check(self):
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = names - installed

        if missing:
            self.install(missing)

    def install(self, missing):
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", *missing],
            stdout=subprocess.DEVNULL,
        )


CheckPackage().check()
