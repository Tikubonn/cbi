
# cbi

cbi is a small preprocessor language written in python.
it wrote for me, so probably it has bug.
i wrote it, because i think, standard cpp is not usefull at some case.
exactly, i dont like escape newlines in multiline block and somethings.
@if oprand was extended of meaning.
@if oprand can use text that will translate to immediate formula.
so, you can use conditional or eternal recursive call. it is my hobby.
@import operand load the source code that was not loaded, so we not have to use include-guard oft.

## overview

example.h
```
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
```	
@import example.h

int main (){
  makebuff(temp, 4096);
  return sum(3);
}
```
example.com.c
```
struct buff {
  void *sequence;
  void *wseek;
  void *rseek;
  void *end;
}

int main (){
  char name ## sequence[size];
  buff name; buff->sequence = sequential;
  buff->wseek = sequential;
  buff->rseek = sequential;
  buff->end = sequential + size;
  return 3 + 3 - 1 + 3 - 1 - 1 + 0;
}
```
