# e-diary-fix

Allows you to fix bad marks, remove chastisements and make comendations.
For every function to use some models must be imported:
```
from datacenter.models import {model}
```

### fix_marks

This function allows you to fix marks, to use it type the following (`Schoolkid` and
`Mark` must be imported):

```
fix_marks({schoolkid name})
```

### remove_chastisements

To remove the unwanted chastisements use(`Schoolkid` must be imported):
```
remove_chastisements({schoolkid name})
```

### create_commendation

To create a commendation use(`Schoolkid`, `Subject`, `Lesson` and `Commendation` 
must be imported):
```
create_commendation({schoolkid name}, {subject name})
```