# sceptre-example

Just a little example for myself to run some
[Sceptre](https://github.com/Sceptre/sceptre) commands.

## Usage

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

aws-vault exec hsw
sceptre launch hsw
```

## Cleanup

Empty the buckets first.

```bash
sceptre delete hsw
```
