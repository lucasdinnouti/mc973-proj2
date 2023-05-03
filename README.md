# RISC-V - SIMULATOR

## Requisites

Before running the simulor, make sure you have these apps installed.

* Python3
* riscv64-unknown-elf-objcopy

## Programs

Considering compiled programs in elf format.

Reference: https://drive.google.com/drive/u/1/folders/1ei8E-qk2dwQvCWJv8ovGJiIdLjw7yVfP

## Running for all test programs

To make it easier, you can run the simulator for all programs in a folter.

```
./run.sh <FOLDER>
```

For example:

```
./run.sh ./test
```

The output log files will be saved in the ./test folder.

## Running for a single program

### Convert program files to .bin

The simulator expects to read binary files. To convert the given elf file, please run the convertion script:

```
./convert.sh
```

This script uses objcopy.

### Execution

For getting the program execution logs, just run:

```
python3 main.py tests/<PROGRAM>
```

For example:

```
python3 main.py tests/000.main.riscv
```

This will generate a log file on the `./test` folder. To change this folder, use `OUTPUT_FOLDER` environment variable.

```
OUTPUT_FOLDER=other-file python3 main.py tests/000.main.riscv
```