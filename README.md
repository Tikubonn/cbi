
# cbi

cbi is a small preprocessor language written in python.
probably it has  bug, because it wrote for me.
i wrote this because, i think, standard cpp is not useful at some case.
i dont like escape newline in multiline block.
maybe some person say "should use snippets or some software".
but, i want to type the source code smoothly.

## functions

* supporting local scope.
* supporting conditional or eternal recursive call.
* supporting `@import` operator. it load sourcecode which is not loaded.

## overview

example.h
```c
struct buff {
  void *sequence;
  void *wseek;
  void *rseek;
  void *end;
}

@define initbuff(buff, sequential, size)
buff->sequence = sequential;
buff->wseek = sequential;
buff->rseek = sequential;
buff->end = sequential + size;
@end

@define makebuff(name, size)
char name ## sequence[size];
buff name; initbuff(&name, name ## sequence, size);
@end

@define sum(num)
@if num @then num + sum(num -1) @else 0 @endif
@end
```

example.c
```c	
@import "example.h"
@import "example.h" // not load again.

int main (){
  makebuff(temp, 4096);
  return sum(3);
}
```

shell
```bash
$ python cbi.py example.c
```

example.com.c
```c
struct buff {
  void *sequence;
  void *wseek;
  void *rseek;
  void *end;
}

int main (){
  char tempsequence[size];
  buff name; buff->sequence = tempsequence;
  buff->wseek = tempsequence;
  buff->rseek = tempsequence;
  buff->end = tempsequence + size;
  return 3 + 3 - 1 + 3 - 1 - 1 + 0;
}
```

## todo
* at now version, ## operator will consolidated tokens in anywhere. so i want to ignore concatenation in outside of block.
* translating to recrusive call to loop.
* think more about order of operators.
* and fix some bug.

## licence
this released under the *MIT Licence*.
