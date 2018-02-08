from doit.tools import run_once

filenames = ['502nmos.zip', '656nmos.zip', '673nmos.zip']
base_url = "https://www.spacetelescope.org/static/projects/fits_liberator/datasets/eagle/"

def task_download():
  actions = []
  for filename in filenames:
    actions.append(['wget', base_url + filename])
  return {'actions': actions,
          'targets': filenames,
          'uptodate': [run_once]}

def task_unzip():
  actions = []
  targets = []
  file_dep = []
  for filename in filenames:
    actions.append( ['unzip', '-o', filename] )
    file_dep.append(filename)
    targets.append( filename.replace('.zip', '.fits') )
  return {'actions': actions,
          'file_dep': file_dep,
          'targets': targets}

  def task_blend():
      return {'actions': [['python', 'image_blender.py']],
