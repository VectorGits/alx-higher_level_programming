#!/usr/bin/bash/python3
if __name__ == "__main__":
    # Print names defined by hidden_4 module ./hidden_4.pyc
    import hidden_4
    for x in dir(hidden_4):
        if x[:2] != "__":
            print(x)
