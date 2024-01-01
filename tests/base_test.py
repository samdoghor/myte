import os
import shutil


class BaseTest:
    def setUp(self) -> None:
        super().setUp()
        # create folder to be tested upon and set cwd
        os.mkdir("myte")
        os.chdir("myte")

    def tearDown(self) -> None:
        super().tearDown()
        # delete folder and reset cwd
        os.chdir("..")
        shutil.rmtree("myte")
