# Regex_Generator_for_WAF_Genetic

This repo has some modified according to [original repo](https://github.com/maojui/Regex-Generator)

## Paper

[Regular Expression Generator by using genetic algorithm](https://drive.google.com/file/d/1CBFFy7oX-bE_4VrLFpP7OT4eJDUP4tku/view?usp=sharing)

## How to use

First install

```bash
git clone https://github.com/manhdqhe153129/Regex_Generator_for_WAF_Genetic.git
cd Regex_Generator_for_WAF_Genetic
pip install -r requirements.txt
```

Then you have to have your own ``access.log`` having all your logs. You can download our small log file from [here](https://drive.google.com/file/d/1s2dMWJ81SF5pWG8op6EJPCjp6lLCE9tv/view?usp=sharing)
Run ``preprocessor.py`` to get all whitelist and blacklist data from log file accordingly (Explore ``preprocess.py`` for more detail) 

```bash
python3 preprocess.py
Log file contained data [access.log]: access.log
Get type from log [white, black, both] [both]: both
output dir [data]: data
```

When you get the data seperate from original log, run ``main.py``

```bash
python3 main.py --data-file data/whitelist_uri.txt
```

## Example

```
Target:
    /media/system/css/fields/switcher.min.css?852c3c99beb07406033f85429263d74798ef3b15
    /media/vendor/joomla-custom-elements/css/joomla-alert.min.css?0.2.0
    /installation/template/css/template.min.css?4a0316c0aa05352ee7be88bcaa27e66c
    /media/system/js/core.min.js?17121a112ecec3d656efe5c5f493429c9acf2179
    /media/system/js/showon.min.js?faea9ca18e3e92a6243f66d83d5ff12f01b925bc
    /media/system/js/keepalive.min.js?20ace83a13886af1b0b5f58386fd8adf33f586a3
    /media/system/js/messages.min.js?7425e8d1cb9e4f061d5e30271d6d99b085344117
    ...
    /installation/template/js/template.js?4a0316c0aa05352ee7be88bcaa27e66c
    /media/system/js/joomla-core-loader.min.js?f76614a44039e2bb5becacfb081df5bf015b351d
    /installation/template/images/Joomla-logo-monochrome-horizontal-white.svg
```

## Result
