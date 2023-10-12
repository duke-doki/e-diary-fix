# e-diary-fix

Allows you to fix bad marks, remove chastisements and make comendations.

## Installation

To use these scripts you need to download `scripts.py` on your server. 
Then run the following commands:
```
python manage.py shell
```
```
import scripts
```

### fix_marks

This function allows you to fix marks, to use it type the following:

```
scripts.fix_marks({schoolkid name})
```

### remove_chastisements

To remove the unwanted chastisements use:
```
scripts.remove_chastisements({schoolkid name})
```

### create_commendation

To create a commendation use:
```
scripts.create_commendation({schoolkid name}, {subject name})
```

`commends.txt` contains variations of commendations that can me edited.