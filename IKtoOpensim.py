import opensim as osim
import os


file_address=r'input_your_.trc_address'

def get_file_paths_with_extension(folder_path, file_extension):
    # 列出文件夹中的所有文件和目录
    all_files = os.listdir(folder_path)

    # 过滤出特定后缀的文件
    specific_files = [f for f in all_files if f.endswith(file_extension)]

    # 生成文件的完整路径
    file_paths = [os.path.join(folder_path, f) for f in specific_files]

    return file_paths



folder_path = file_address
file_extension = '.trc'
file_paths = get_file_paths_with_extension(folder_path, file_extension)
file_paths = [item.replace('\\', '/') for item in file_paths]
print(file_paths)

for i in range(len(file_paths)):
    model = osim.Model(f'{i}.osim')
    model.finalizeConnections()
    ik_tool = osim.InverseKinematicsTool()
    ik_tool.setModel(model)
    ik_tool.setMarkerDataFileName(file_paths[i])
    ik_tool.setOutputMotionFileName(f'ik{i}.mot')
    ik_tool.run()





