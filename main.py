import os
import random
import sys
import time
import argparse
import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim



def main(mode,model='dqn',gamma=0.99,final_epsilon=0.0001,initial_epsilon=0.1,number_of_iterations=2000000,replay_memory_size=10000,minibatch_size=32):
    os.makedirs('pretrained_model', exist_ok=True)
    if model == 'dqn':
        import dqn as dqn
    elif model == 'double_dqn':
        import double_dqn as dqn
    elif model == 'dueling_dqn':
        import dueling_dqn as dqn
    
    dqn.main(mode,gamma,final_epsilon,initial_epsilon,number_of_iterations,replay_memory_size,minibatch_size)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flappy Bird with Reinforcement Learning')
    parser.add_argument('-mode', '--mode', type=str, default='train', help='Mode: train or test')
    parser.add_argument('-m', '--model', type=str, default='dqn', help='Model to use: dqn or double_dqn')
    parser.add_argument('-g', '--gamma', type=float, default=0.99, help='Discount factor')
    parser.add_argument('-fe', '--final_epsilon', type=float, default=0.0001, help='Final epsilon value')
    parser.add_argument('-ie', '--initial_epsilon', type=float, default=0.1, help='Initial epsilon value')
    parser.add_argument('-n', '--number_of_iterations', type=int, default=2000000, help='Number of iterations')
    parser.add_argument('-r', '--replay_memory_size', type=int, default=10000, help='Replay memory size')
    parser.add_argument('-b', '--minibatch_size', type=int, default=32, help='Minibatch size')
    args = parser.parse_args()
    main(args.mode,args.model,args.gamma,args.final_epsilon,args.initial_epsilon,args.number_of_iterations,args.replay_memory_size,args.minibatch_size)

