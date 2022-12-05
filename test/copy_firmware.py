import shutil
import os

Import("env")

def post_program_action(source, target, env):
    project_root = env['PROJECT_DIR']
    release_dir = os.path.join(project_root, 'release')
    program_path = target[0].get_abspath()  
    shutil.copy(program_path, release_dir)

env.AddPostAction("$BUILD_DIR/${PROGNAME}.elf", post_program_action)
env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", post_program_action)
