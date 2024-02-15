
import os
import sys
import subprocess
import shutil

subprocess.run([
  'cargo', 'run', '--release', '--bin', 'hg-view', '--'
], check=True)
