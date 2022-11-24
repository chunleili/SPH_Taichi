# 测试使用json读取场景文件参数

import json

def test_json():
    scene_file_path = 'E:\Dev\SPH_Taichi\data\scenes\dragon_bath.json'
    with open(scene_file_path, "r") as f:
        config = json.load(f)

    # get all data
    print('---------get all data----------')
    print(config)

    # get density0
    print('---------get density0----------')
    someKey = 'Configuration'
    someValue = 'density0'
    density0 = config[someKey][someValue]
    print(density0)
    print(type(density0))

    # get gravitation
    print('---------get gravitation----------')
    someKey2 = 'Configuration'
    someValue2 = 'gravitation'
    gravitation = config[someKey2][someValue2]
    print(gravitation)
    print(type(gravitation))

    # # get geometryFile
    print('---------get geometryFile----------')
    rbs = config["RigidBodies"]
    geometryFile=rbs[0]['geometryFile']
    print(geometryFile)
    print(type(geometryFile))


if __name__ == '__main__':
    test_json()