<div align="center">
    <img src="https://github.com/ibnaleem/paskell/blob/main/docs/paskell.png?raw=true">
</div>
    
<p align="center">a Python package that communicates between Python and Haskell</p>

<div align="center">
    <a href="https://www.buymeacoffee.com/ibnaleem" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</div>

<div align="center">

<a href="https://github.com/ibnaleem/paskell/stargazers"><img src="https://img.shields.io/github/stars/ibnaleem/paskell.svg?style=for-the-badge"></a>
<a href="https://github.com/ibnaleem/paskell/blob/main/LICENSE"><img src="https://img.shields.io/github/license/ibnaleem/paskell?style=for-the-badge"></a>
</div>

## Installation
```shell
pip install paskell
```
```shell
python3 pip install paskell
```

## Usage
Paskell **requires** your Haskell file has been fully compiled and can run as an executable. For Windows users, their Haskell file must be `{file_name}.exe`, and for Unix users it should be `./{file_name}`
Paskell will **not run** your Haskell file if it was not compiled. 
```python
import paskell

haskell_file = "path_to_haskell_file"
result = paskell.run(haskell_file, input_data="input data as string") # input data is optional
print(result)
```

## Contributing
I welcome contributions from the community and appreciate the time and effort put into making [Paskell](https://github.com/ibnaleem/paskell) better. To contribute, please follow the guidelines and steps outlined below:

> Note: **_Your pull request will be closed if you do not specify the changes you've made._**

### Fork the Repository
Start by [forking this repository](https://github.com/ibnaleem/paskell/fork). You can do this by clicking on the ["Fork"](https://github.com/ibnaleem/paskell/fork) button located at the top right corner of the GitHub page. This will create a personal copy of the repository under your own GitHub account.

### Clone the Repository
Next, clone the forked repository to your local machine using the following command:
```bash
$ git clone https://github.com/yourusername/paskell.git
```
Navigate to the cloned directory:
```bash 
$ cd paskell
```
### Create a New Branch
Before making any changes, it's recommended to create a new branch. This ensures that your changes won't interfere with other contributions and keeps the main branch clean. Use the following command to create and switch to a new branch:
```bash
$ git checkout -b branch-name
```
### Make the Desired Changes
Now, you can proceed to make your desired changes to the project. Whether it's fixing bugs, adding new features, improving README, or optimizing code, your efforts will be instrumental in enhancing the project.

### Commit and Push Changes
Once you have made the necessary changes, commit your work using the following commands:
```bash
$ git add .
$ git commit -m "Your commit message"
```
Push the changes to your forked repository:
```bash
$ git push origin branch-name
```
### Submit a Pull Request
Head over to the [original repository](https://github.com/ibnaleem/paskell) on GitHub and go to the ["Pull requests"](https://github.com/ibnaleem/paskell/pulls) tab.
1. Click on the "New pull request" button.
2. Select your forked repository and the branch containing your changes.
3. Provide a clear and informative title for your pull request, and use the description box to explain the modifications you have made. **_Your pull request will be closed if you do not specify the changes you've made._**
4. Finally, click on the "Create pull request" button to submit your changes.

## PGP Fingerprint
```
2024 7EC0 23F2 769E 6618  1C0F 581B 4A2A 862B BADE
```
