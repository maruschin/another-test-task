# another-test-task


### Installation

```
pip install https://github.com/maruschin/another-test-task.git
```

### Command to show all arguments
```
$ python -m anothertt -h
```

```
usage: anotherttt [-h] [-W WIDTH] [-H HEIGHT] [-K CURVATURE] [-N ITERATIONS]
               [--out OUT]

Triangular application.

optional arguments:
  -h, --help            show this help message and exit
  -W WIDTH, --width WIDTH
                        figure width
  -H HEIGHT, --height HEIGHT
                        figure height
  -K CURVATURE, --curvature CURVATURE
                        curvature coefficient
  -N ITERATIONS, --iterations ITERATIONS
                        number of iterations
  --out OUT
```


### Examples
```
python -m anothertt -W 300 -H 200 -N 5 -K 0.1 --out fig.png
```
A folder with logs and a file with an image will be created in the running directory.

