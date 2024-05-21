# Using DQN to Solve Flappy Bird



##### Dependencies:
* Python 3.9.13
* Run `pip3 install -r requirements.txt` to install dependencies.

##### How to run:
* Download the pretrained models from [github](https://github.com/dtungpka/Flappybird-RNN-A) and put them in the `pretrained_model` folder.
* Run `python train.py -mode test -m dqn` to run pretrained dqn model.
* Run `python train.py -mode train -m double_dqn` to train dqn model.

##### Usage:
```
usage: main.py [-h] [-mode MODE] [-m MODEL] [-g GAMMA] [-fe FINAL_EPSILON] [-ie INITIAL_EPSILON]
               [-n NUMBER_OF_ITERATIONS] [-r REPLAY_MEMORY_SIZE] [-b MINIBATCH_SIZE]

Flappy Bird with Reinforcement Learning

optional arguments:
  -h, --help            show this help message and exit
  -mode MODE, --mode MODE
                        Mode: train or test
  -m MODEL, --model MODEL
                        Model to use: dqn , double_dqn or dueling_dqn
  -g GAMMA, --gamma GAMMA
                        Discount factor
  -fe FINAL_EPSILON, --final_epsilon FINAL_EPSILON
                        Final epsilon value
  -ie INITIAL_EPSILON, --initial_epsilon INITIAL_EPSILON
                        Initial epsilon value
  -n NUMBER_OF_ITERATIONS, --number_of_iterations NUMBER_OF_ITERATIONS
                        Number of iterations
  -r REPLAY_MEMORY_SIZE, --replay_memory_size REPLAY_MEMORY_SIZE
                        Replay memory size
  -b MINIBATCH_SIZE, --minibatch_size MINIBATCH_SIZE
                        Minibatch size

```



