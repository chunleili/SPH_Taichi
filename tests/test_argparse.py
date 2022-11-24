# 测试使用 argparse 读取命令行参数

import argparse

def test_argparse():
    parse = argparse.ArgumentParser(description='test argparse')
    parse.add_argument('--par', default='blabla', help='some-help')
    parse.add_argument('--ILove', default='you', help='some-help')
    arg2 = parse.parse_args()
    print('the arguments:')
    print(arg2.par)
    print(arg2.ILove)
    

if __name__ == '__main__':
    test_argparse()