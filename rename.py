import os
import yaml
from datetime import datetime, date
import portalocker

# 指定Markdown文件所在的根目录
root_directory = 'MATH'

# 遍历根目录及其所有子目录中的所有Markdown文件
for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith('.md'):
            filepath = os.path.join(dirpath, filename)
            
            try:
                # 先以文本模式读取文件内容
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # 检查文件是否包含YAML前言
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end != -1:
                        yaml_content = content[3:yaml_end].strip()
                        try:
                            # 解析YAML内容
                            yaml_data = yaml.safe_load(yaml_content)
                            if 'date' in yaml_data:
                                # 提取日期并格式化
                                date_value = yaml_data['date']
                                formatted_date = date_value.strftime('%Y-%m-%d') if isinstance(date_value, (datetime, date)) else datetime.strptime(date_value, '%Y-%m-%d').strftime('%Y-%m-%d')
                                
                                # 生成新的文件名
                                new_filename = f"{formatted_date} {filename}"
                                new_filepath = os.path.join(dirpath, new_filename)
                                
                                # 以二进制模式重新打开文件进行锁定和重命名
                                with open(filepath, 'r+b') as file:
                                    portalocker.lock(file, portalocker.LOCK_EX)  # 独占锁
                                    
                                    # 重命名文件
                                    os.rename(filepath, new_filepath)
                                    print(f"Renamed: {filepath} -> {new_filepath}")
                        except yaml.YAMLError as e:
                            print(f"Error parsing YAML in file {filename}: {e}")
                        except Exception as e:
                            print(f"Error processing file {filename}: {e}")
                else:
                    print(f"No YAML front matter found in file {filename}")
            except portalocker.exceptions.LockException as e:
                print(f"Could not lock file {filename}: {e}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")