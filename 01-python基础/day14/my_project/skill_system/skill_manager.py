
import sys
# 导包是否成功？
# 取决于sys.path中的路径与from的路径是否可以正确找到文件.
sys.path.append('/home/tarena/1908/month01/code/day14/my_project')
print(sys.path)

from skill_system.skill_deployer import *

class SkillManager:
    def get_skill(self):
        print("SkillManager　-- get_skill")

SkillDeployer().generate_skll()