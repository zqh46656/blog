---
date: 2026-10-12 12:00:00
tags: 公告
stream: math
extra:
  math: true
---

# 如何定义自然数、整数、有理数、实数


## 本文目录<br>
<br>
第一章  自然数及其加法运算<br>
第二章  自然数的乘法运算<br>
第三章  自然数的序<br>
第四章  整数<br>
第五章  有理数<br>
第六章  实数<br>
第七章  正实数的进制表示（补充内容）<br>
<br>
最近跟一位朋友讲了点这方面的东西，正好把它整理出来。<br>
<br>
我们先从自然数开始。<br>
<br>
自然数的基本规则是众所周知的五条自然数公理，也叫 Peano 公理：<br>
① $0$ 是自然数；<br>
② 每个自然数 $n$ 都有唯一的后继数 $n'$，$n'$ 也是自然数；<br>
③ $0$ 不是任何自然数的后继数；<br>
④ 不同自然数的后继数不同；<br>
⑤ 若 $P(\cdot)$ 是一个性质（即谓词），$P(0)$ 成立，且对任意自然数 $n$，若 $P(n)$ 成立，则 $P(n')$ 成立，则对任意自然数 $n$，都有 $P(n)$ 成立。<br>
<br>
可以写成一阶逻辑，设 $\operatorname{Nat}(\cdot)$ 是固定的一元谓词（代表“是自然数”），$0$ 是常项（代表熟知的零），$\operatorname{succ}(\cdot)$ 是一元函项（代表“后继数”），$=$ 为等词，$m,n$ 是变项。<br>
一阶逻辑里等词的公理是：对全体谓词 $P$，都有公理 $(x=y)\to(P(\dots,x,\dots)\to P(\dots,y,\dots))$，被省略的部分是一致的变项。<br>
那么五条公理分别对应：<br>
① $\operatorname{Nat}(0)$；<br>
② $\forall n : \operatorname{Nat}(n)\to \operatorname{Nat}(\operatorname{succ}(n))$；<br>
③ $\forall n : \operatorname{Nat}(n)\to\neg(\operatorname{succ}(n)=0)$；<br>
④ $\forall m : (\forall n : ( \operatorname{Nat}(m)\land \operatorname{Nat}(n) )\to( (\operatorname{succ}(m)=\operatorname{succ}(n))\to(m=n) ) )$<br>
⑤ 对全体一元谓词 $P$，都有公理<br>
$$
P(0)\land(\forall n : \operatorname{Nat}(n)\to( P(n)\to P(\operatorname{succ}(n)) ) ) \to (\forall n : \operatorname{Nat}(n)\to P(n) ) .
$$<br>

不过如果要严格化，一些细节还需要一点点递归论。所以后续我们还是用更加朴素的表述而不是这种逻辑化的表述。<br>

<br>


## 第一章  自然数及其加法运算

<br>
自然数上面最重要的结构是三个：加法、乘法、序。<br>
我们将自然数集记为 $\mathbb{N}$ ，然后开始定义。<br>
<br>
先定义加法：存在唯一的运算 $+: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ ，使得<br>
① $a+0=a$ ；<br>
② $a+b'=(a+b)'$ .<br>
<br>
$a+b$ 结果的唯一性可以通过对 $b$ 归纳得到。首先 $a+0$ 有唯一确定的结果 $a$ ，然后，若 $a+b$ 有唯一确定的结果，则 $a+b'=(a+b)'$ 确保 $a+b'$ 也有唯一确定的结果，所以对任意自然数 $a,b$ ，$a+b$ 都有唯一确定的结果.<br>
<br>
接下来就是研究加法运算的性质了。<br>
<br>
<b>命题 1.1</b>：$(a+b)+c=a+(b+c)$ .<br>
<b>证明</b>　对 $c$ 归纳：<br>
一方面，有 $(a+b)+0=a+b=a+(b+0)$ ；<br>
另一方面，若 $(a+b)+c=a+(b+c)$ ，则 $(a+b)+c'=((a+b)+c)'=(a+(b+c))'=a+(b+c)'=a+(b+c')$ .<br>
所以根据数学归纳法，有 $(a+b)+c=a+(b+c)$ . $\blacksquare$<br>
<br>
<b>命题 1.2</b>：$0+a=a$ .<br>
<b>证明</b>　对 $a$ 归纳：<br>
一方面，有 $0+0=0$；<br>
另一方面，若 $0+a=a$ ，则 $0+a'=(0+a)'=a'$ .<br>
所以根据数学归纳法，有 $0+a=a$ . $\blacksquare$<br>
<br>
<b>命题 1.3</b>：$0'+a=a'$ .<br>
<b>证明</b>　对 $a$ 归纳：<br>
一方面，有 $0'+0=0'$；<br>
另一方面，若 $0'+a=a'$ ，则 $0'+a'=(0'+a)'=(a')'$ .<br>
所以根据数学归纳法，有 $0'+a=a'$ . $\blacksquare$<br>
<br>
<b>命题 1.4</b>：$a+b=b+a$ .<br>
<b>证明</b>　对 $b$ 归纳，注意这里归纳证明的结论里 $a$ 被全称量词约束，即结论是「对任意自然数 $a$ 有 $a+b=b+a$」：<br>
一方面，根据命题 1.2 有 $0+a=a=a+0$ ，所以对任意自然数 $a$ 有 $a+0=0+a$ ；<br>
另一方面，若对任意自然数 $a$ 有 $a+b=b+a$ ，<br>
则对自然数 $a$ ，又有 $a'+b=b+a'$ .<br>
根据命题 1.1 有 $a+(0'+b)=(a+0')+b$ ，根据性质 3 有 $a'=0'+a$ ，所以 $a+b'=a+(0'+b)=(a+0')+b=(a+0)'+b=a'+b=b+a'=b+(0'+a)=(b+0')+a=(b+0)'+a=b'+a$ .<br>
这就说明对任意自然数 $a$ ，有 $a+b'=b'+a$ .<br>
所以根据数学归纳法，对任意自然数 $a$ ，有 $a+b=b+a$ . $\blacksquare$<br>
<br>
<b>命题 1.5</b>：$a'+b=a+b'$ .<br>
<b>证明</b>　直接利用命题 1.4 得到 $a+b=b+a$ ，从而 $a'+b=b+a'=(b+a)'=(a+b)'=a+b'$ . $\blacksquare$<br>
<br><br>
至此，由于命题 1.1 和命题 1.4 ，我们可以直接书写 $a+b+c$ 而无需担心歧义，也可以轻易交换运算的前后顺序。同时，两个自然数相加时，根据命题 1.5 ，后继符号可以从一个自然数转移到另一个自然数。<br>

<br><br>


## 第二章  自然数的乘法运算<br>
<br>
然后定义乘法：存在唯一的运算 $\cdot: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ ，使得<br>
① $a \cdot 0=0$ ；<br>
② $a \cdot b'=a \cdot b+a$ .<br>
<b>注意在乘法和加法同时书写时，优先计算乘法。</b><br>
<br>
$a \cdot b$ 结果的唯一性可以通过对 $b$ 归纳得到。首先 $a \cdot 0$ 有唯一确定的结果 $0$ ，然后，若 $a \cdot b$ 有唯一确定的结果，则 $a \cdot b'=a \cdot b+a$ 确保 $a \cdot b'$ 也有唯一确定的结果，所以对任意自然数 $a,b$ ，$a \cdot b$ 都有唯一确定的结果.<br>
<br>
接下来证明一些乘法运算的性质。<br>
<br>
<b>命题 2.1</b>：$(a+b) \cdot c=a \cdot c+b \cdot c$ .<br>
<b>证明</b>　对 $c$ 归纳：<br>
一方面，有 $(a+b) \cdot 0=0=0+0=a \cdot 0+b \cdot 0$ ；<br>
另一方面，若 $(a+b) \cdot c=a \cdot c+b \cdot c$ ，则 $(a+b) \cdot c'=(a+b) \cdot c+(a+b)=(a \cdot c+b \cdot c)+(a+b)=(a \cdot c+a)+(b \cdot c+b)=a \cdot c'+b \cdot c'$ .<br>
所以根据数学归纳法，有 $(a+b) \cdot c=a \cdot c+b \cdot c$ . $\blacksquare$<br>
<br>
<b>命题 2.2</b>：$c \cdot (a+b)=c \cdot a+c \cdot b$ .<br>
<b>证明</b>　对 $b$ 归纳：<br>
一方面，有 $c \cdot (a+0)=c \cdot a=c \cdot a+0=c \cdot a+c \cdot 0$ ；<br>
另一方面，若 $c \cdot (a+b)=c \cdot a+c \cdot b$ ，则 $c \cdot (a+b')=c \cdot (a+b)'=c \cdot (a+b)+c=c \cdot a+c \cdot b+c=c \cdot a+c \cdot b'$ .<br>
所以根据数学归纳法，有 $c \cdot (a+b)=c \cdot a+c \cdot b$ . $\blacksquare$<br>
<br>
<b>命题 2.3</b>：$0 \cdot a=0$ .<br>
<b>证明</b>　对 $a$ 归纳：<br>
一方面，有 $0 \cdot 0=0$ ；<br>
另一方面，若 $0 \cdot a=0$ ，则 $0 \cdot a'=0 \cdot a+0=0 \cdot a=0$ .<br>
所以根据数学归纳法，有 $0 \cdot a=0$ . $\blacksquare$<br>
<br>
<b>命题 2.4</b>：$(a \cdot b) \cdot c=a \cdot (b \cdot c)$ .<br>
<b>证明</b>　对 $c$ 归纳：<br>
一方面，有 $(a \cdot b) \cdot 0=0=a \cdot 0=a \cdot (b \cdot 0)$ ；<br>
另一方面，若 $(a \cdot b) \cdot c=a \cdot (b \cdot c)$ ，根据命题 2.2 有 $a \cdot (b \cdot c)+a \cdot b=a \cdot (b \cdot c+b)$ ，<br>
故 $(a \cdot b) \cdot c'=(a \cdot b) \cdot c+a \cdot b=a \cdot (b \cdot c)+a \cdot b=a \cdot (b \cdot c+b)=a \cdot (b \cdot c')$ .<br>
所以根据数学归纳法，有 $(a \cdot b) \cdot c=a \cdot (b \cdot c)$ . $\blacksquare$<br>
<br>
<b>命题 2.5</b>：$0' \cdot a=a$ .<br>
<b>证明</b>　对 $a$ 归纳：<br>
一方面，有 $0' \cdot 0=0$ ；<br>
另一方面，若 $0' \cdot a=a$ ，则 $0' \cdot a'=0' \cdot a+0'=a+0'=(a+0)'=a'$ .<br>
所以根据数学归纳法，有 $0' \cdot a=a$ . $\blacksquare$<br>
<br>
<b>命题 2.6</b>：$a \cdot b=b \cdot a$ .<br>
<b>证明</b>　对 $b$ 归纳：<br>
一方面，根据命题 2.3 有 $0 \cdot a=0$ ，所以 $a \cdot 0=0=0 \cdot a$ ；<br>
另一方面，若 $a \cdot b=b \cdot a$ ，则根据命题 2.5 有 $0' \cdot a=a$ ，故 $a \cdot b'=a \cdot b+a=b \cdot a+a=b \cdot a+0' \cdot a=(b+0') \cdot a=(b+0)' \cdot a=b' \cdot a$ .<br>
所以根据数学归纳法，有 $a \cdot b=b \cdot a$ . $\blacksquare$<br>
<br><br>
至此我们证明了：乘法交换律、乘法结合律、乘法关于加法的分配律。<br>
<br>
接下来单独定义 $\mathbb{N}$ 上的一个偏序，然后证明一些较为重要的命题。<br>

<br><br>


## 第三章  自然数的序<br>
<br>
先证明两个有些奇怪的命题。这两个命题的共性是：我们使用数学归纳法的归纳推理部分时，只需要使用 $n$ 是某个数的后继数，而无需使用归纳假设本身。<br>
<br>
<b>命题 3.1</b>：若 $a+b=0$ ，则 $a=0$ .<br>
<b>证明</b>　对 $b$ 归纳：<br>
一方面，若 $b=0$ ，则结论为「若 $a+0=0$ ，则 $a=0$ 」，显然成立；<br>
另一方面，如果已经有「若 $a+b=0$ ，则 $a=0$ 」（这个归纳假设不需要使用），由于 $a+b'=(a+b)'\neq 0$，故「若 $a+b'=0$ ，则 $a=0$ 」直接成立。<br>
所以根据数学归纳法可得：若 $a+b=0$ ，则 $a=0$ . $\blacksquare$<br>
<br>
<i>注：交换 $a,b$ 的顺序，即可和原结论共同得到：若 $a+b=0$ ，则 $a=0$ ，$b=0$ .　此后将不加说明，直接使用。</i><br>
<br>
<b>命题 3.2</b>：若 $a\neq 0$ ，则 $a$ 是某个自然数的后继数.<br>
<b>证明</b>　对 $a$ 归纳：<br>
一方面，$0\neq 0$ 不可能成立，所以「若 $0\neq 0$ ，则 $0$ 是某个自然数的后继数」直接成立；<br>
另一方面，如果已经有「若 $a\neq 0$ ，则 $a$ 是某个自然数的后继数」（这个归纳假设不需要使用），<br>
由于 $a'$ 是 $a$ 的后继数，所以 $a'$ 是某个自然数的后继数，从而「若 $a'\neq 0$ ，则 $a'$ 是某个自然数的后继数」成立。<br>
所以根据数学归纳法可得：若 $a\neq 0$ ，则 $a$ 是某个自然数的后继数。 $\blacksquare$<br>
<br>
<i>根据以上两个命题的证明可得一个推论：若一个性质对 $0$ 成立，且对任意自然数的后继数成立，那么这个性质对任意自然数成立。</i><br>
<br>
<b>命题 3.3</b>：若 $a+c=b+c$ ，则 $a=b$ .<br>
<b>证明</b>　对 $c$ 归纳：<br>
一方面，结论对 $c=0$ 显然成立；<br>
另一方面，如果已经有「若 $a+c=b+c$ ，则 $a=b$ 」，若 $a+c'=b+c'$ ，则 $(a+c)'=(b+c)'$ .<br>
由于不同自然数的后继数不同，故 $a+c=b+c$ ，从而 $a=b$ .<br>
这就得到「若 $a+c'=b+c'$ ，则 $a=b$ 」。<br>
所以根据数学归纳法可得：若 $a+c=b+c$ ，则 $a=b$ . $\blacksquare$<br>
<br>
接下来定义序。<br>
<br>
我们定义 $\mathbb{N}$ 上的一个序 $\le$ ，<b>若自然数 $a,b$ 满足：存在自然数 $u$ ，使得 $a+u=b$ ，则规定 $a\le b$ .</b><br>
<br>
然后我们证明这确实是一个偏序关系。<br>
<br>
<b>命题 3.4</b>：$\le$ 是一个偏序关系.<br>
<b>证明</b>　①自反性：根据 $a+0=a$ ，可得 $a\le a$ ；<br>
<br>
②传递性：若 $a\le b$ ，$b\le c$ ，设 $a+u=b$ ，$b+v=c$ ，则 $a+(u+v)=(a+u)+v=b+v=c$ ，所以 $a\le c$ ；<br>
<br>
③反对称性：若 $a\le b$ ，$b\le a$ ，设 $a+u=b$ ，$b+v=a$ ，则 $(a+b)+(u+v)=(a+u)+(b+v)=b+a=a+b=(a+b)+0$ .<br>
根据命题 3.3 有 $u+v=0$ ，再根据命题 3.1 有 $u=v=0$ ，从而 $a=b+v=b+0=b$ .<br>
<br>
这样就证明了 $\le$ 是一个偏序关系。 $\blacksquare$<br>
<br>
下面证明 $\le$ 还是线性序：<br>
<br>
<b>命题 3.5</b>：$0\le a$ .<br>
<b>证明</b>　由于 $0+a=a$ ，故 $0\le a$ . $\blacksquare$<br>
<br>
<b>命题 3.6</b>：$a\le b$ 或 $b\le a$ .<br>
<b>证明</b>　对 $b$ 归纳：<br>
一方面，根据命题 3.5 有 $0\le a$ ，故 $a\le 0$ 或 $0\le a$ 显然成立；<br>
另一方面，若 $a\le b$ 或 $b\le a$ ：<br>
——如果 $a\le b$ ，设 $a+u=b$ ，则 $a+u'=(a+u)'=b'$ ，所以 $a\le b'$ ，从而 $a\le b'$ 或 $b'\le a$ .<br>
——如果 $b\le a$ ，可设 $b+v=a$ .<br>
————如果 $v=0$ ，则 $a=b+v=b+0=b$ ，所以 $a+0'=b+0'=(b+0)'=b'$ ，所以 $a\le b'$ ，从而 $a\le b'$ 或 $b'\le a$ .<br>
————如果 $v\neq 0$ ，则根据命题 3.2 ，存在自然数 $w$ 使得 $v=w'$ ，故 $a=b+v=b+w'=b'+w$，所以 $b'\le a$ ，从而 $a\le b'$ 或 $b'\le a$ .<br>
这就得到了 $a\le b'$ 或 $b'\le a$ .<br>
所以根据数学归纳法，有 $a\le b$ 或 $b\le a$ .<br>
<br>
至此我们证明了 $\le$ 是线性序。之后，$a\ge b$ 表示 $b\le a$ ；$a\lt b$ 表示 $a\le b$ 且 $a\neq b$ ，$a\gt b$ 表示 $b\lt a$ .<br>
<br>
而对于线性序 $\le$ ，对任意 $a,b$ ，三个结论 $a\lt b$ ，$a=b$ ，$a\gt b$ 总是恰有一个成立。<br>
<br>
最后证明一个非常重要的性质：$\le$ 是良序。 $\blacksquare$<br>
<br>
<b>命题 3.7</b>：若 $a\lt b$ ，则 $a'\le b$ .<br>
<b>证明</b>　由于 $a\le b$ ，可设 $a+u=b$ ，而 $a\neq b$ ，假设 $u=0$ 则有 $b=a+u=a+0=a$ ，矛盾，故 $u\neq 0$ .<br>
根据命题 3.2 ，存在 $v$ 使得 $u=v'$ ，故 $b=a+u=a+v'=a'+v$ ，所以 $a'\le b$ . $\blacksquare$<br>
<br>
<b>命题 3.8</b>：若 $L$ 是 $\mathbb{N}$ 的非空子集，则 $L$ 存在一个最小元素.<br>
<b>证明</b>　假设结论不成立，那么存在一个 $\mathbb{N}$ 的非空子集 $L$ ，使得 $L$ 没有最小元素。<br>
下面用数学归纳法证明：对任意自然数 $n$ ，都有对任意 $m\in L$ ，有 $n\le m$ .<br>
对 $n$ 归纳：<br>
——一方面，当 $n=0$ 时，结论显然成立；<br>
——另一方面，如果对任意自然数 $n$ ，都有对任意 $m\in L$ ，有 $n\le m$ .<br>
——假设 $n\in L$ ，则 $n\in L$ 的同时，还有对任意 $m\in L$ ，有 $n\le m$ ，这意味着 $n$ 是 $L$ 的最小元素，矛盾。<br>
——所以 $n$ 不属于 $L$ ，这表明对任意 $m\in L$ ，有 $n\neq m$ .<br>
——从而对任意 $m\in L$ ，有 $n\le m$ 且 $n\neq m$ ，即 $n\lt m$ ，故根据命题 3.7 有 $n'\le m$ .<br>
——这就得到对任意 $m\in L$ ，有 $n'\le m$ .<br>
所以根据数学归纳法，对任意自然数 $n$ ，都有对任意 $m\in L$ ，有 $n\le m$ .<br>
任取 $k\in L$ ，然后在这个结论中取 $n=k'$ ，则对任意 $m\in L$ ，有 $k'\le m$ .<br>
再取 $m=k$ ，即可得到 $k'\le k$ .<br>
而根据 $k+0'=(k+0)'=k'$，有 $k\le k'$ ，所以根据 $\le$ 的反对称性有 $k=k'$ ，从而 $k+0=k=k'=(k+0)'=k+0'$ ，根据命题 3.3 有 $0=0'$ ，但 $0$ 不是任何数的后继数，矛盾。<br>
这就说明假设不成立，从而命题 3.8 得证。 $\blacksquare$<br>
<br>
需要特别注意的是，一些高中竞赛书上可能会有「数学归纳法和最小数原理（命题 3.8 ）等价」的说法。然而自然数中的偏序关系本身依赖数学归纳法，从而在没有数学归纳法时，「最小数」的含义是无从谈起的。<br>
<br>
最后补充两个结论：<br>
<br>
<b>命题 3.9</b>：若自然数 $a,b$ 满足 $a\cdot b=0$ ，则 $a=0$ 或 $b=0$ .<br>
<b>证明</b>　假设 $a,b$ 都不是零，根据命题 3.2 ，可设 $a=c'$ ，$b=d'$ .<br>
从而 $0=a\cdot b=c'\cdot d'=c'\cdot d+c'$ ，再根据命题 3.1 有 $c'=0$ ，但 $0$ 不是任何自然数的后继数，矛盾.<br>
所以 $a=0$ 或 $b=0$ . $\blacksquare$<br>
<br>
<b>命题 3.10</b>：自然数 $a,b$ 不可能满足 $a\lt b$ 且 $b\lt a+0'$ .<br>
<b>证明</b>　假设 $a\lt b$ 且 $b\lt a+0'$ ，设 $a+u=b$ ，$b+v=a+0'$ ，且 $u,v$ 都不是零（否则得到小于号两边相等）。<br>
那么 $(a+b)+(u+v)=(a+u)+(b+v)=b+(a+0')=(a+b)+0'$ ，所以根据命题 3.3 有 $u+v=0'$ .<br>
由于 $u,v$ 都不是零，根据命题 3.2 ，存在自然数 $x,y$ 使得 $u=x'$ ，$v=y'$ ，从而 $0'=x'+y'=x'+(y+0)'=x'+y+0'$ .<br>
根据命题 3.3 又有 $x'+y=0$ ，从而根据命题 3.1 有 $x'=0$ ，但 $0$ 不是任何自然数的后继数，矛盾。<br>
所以命题 3.10 得证。 $\blacksquare$<br>

<br><br>


## 第四章  整数<br>
<br>
然后我们可以由自然数定义整数：<br>
<br>
在 $\mathbb{N} \times \mathbb{N}$ 上定义如下等价关系：如果自然数 $a,b,c,d$ 满足 $a+d=b+c$ ，则称 $(a,b)\sim(c,d)$ .<br>
下面证明这确实是等价关系。<br>
①反身性：由于 $a+b=a+b$ ，故 $(a,b)\sim(a,b)$ ；<br>
②对称性：若 $(a,b)\sim(c,d)$ ，则 $a+d=b+c$ ，所以 $c+b=d+a$ ，所以 $(c,d)\sim(a,b)$ .<br>
③传递性：若 $(a,b)\sim(c,d)$ ，$(c,d)\sim(e,f)$ ，则 $a+d=b+c$ ，$c+f=d+e$ ，故 $(a+f)+(c+d)=(a+d)+(c+f)=(b+c)+(d+e)=(b+e)+(c+d)$ ，根据命题 3.3 有 $a+f=b+e$ ，所以 $(a,b)\sim(e,f)$ .<br>
<br>
在这样的等价关系下，全体等价类构成的集合定义为整数集 $\mathbb{Z}$ ，每个等价类是一个整数。将 $(a,b)$ 所在的等价类记为 $\lbrack (a,b) \rbrack$ .<br>
下面将自然数上的加法、乘法和序迁移过来。<br>
<br>
定义加法为：$\lbrack (a,b) \rbrack+\lbrack (c,d) \rbrack=\lbrack (a+c,b+d) \rbrack$；<br>
定义乘法为：$\lbrack (a,b) \rbrack\cdot\lbrack (c,d) \rbrack=\lbrack (a\cdot c+b\cdot d,a\cdot d+b\cdot c) \rbrack$；<br>
定义序为：若 $\lbrack (a,b) \rbrack$ , $\lbrack (c,d) \rbrack$ 满足 $a+d\leq b+c$ ，则规定 $\lbrack (a,b) \rbrack\leq\lbrack (c,d) \rbrack$ .<br>
再同时定义相反数的概念：称 $\lbrack (a,b) \rbrack$ 的相反数为 $\lbrack (b,a) \rbrack$ .<br>
<br>
<b>命题 4.1</b>：$\mathbb{Z}$ 上的加法、乘法、序、相反数都是良定义的.<br>
<b>证明</b>　我们设 $\lbrack (a,b) \rbrack=\lbrack (a^*,b^*) \rbrack$ ，$\lbrack (c,d) \rbrack=\lbrack (c^*,d^*) \rbrack$ ，则 $a+b^*=a^*+b$ ，$c+d^*=c^*+d$ .<br>
(1) 由于 $(a+c)+(b^*+d^*)=(a+b^*)+(c+d^*)=(a^*+b)+(c^*+d)=(a^*+c^*)+(b+d)$ ，故 $\lbrack (a+c,b+d) \rbrack=\lbrack (a^*+c^*,b^*+d^*) \rbrack$ ；<br>
(2) 由于 $$\begin{aligned}
(a\cdot c+b\cdot d)+(a^*\cdot d+b^*\cdot c) &= (a+b^*)\cdot c+(a^*+b)\cdot d \\
&= (a^*+b)\cdot c+(a+b^*)\cdot d = (a\cdot d+b\cdot c)+(a^*\cdot c+b^*\cdot d)
\end{aligned}$$<br>
故 $\lbrack (a\cdot c+b\cdot d,a\cdot d+b\cdot c) \rbrack=\lbrack (a^*\cdot c+b^*\cdot d,a^*\cdot d+b^*\cdot c) \rbrack$ ；<br>
由于 $$\begin{aligned}
(a^*\cdot c+b^*\cdot d)+(a^*\cdot d^*+b^*\cdot c^*) &= a^*\cdot(c+d^*)+b^*\cdot(c^*+d) \\
&= a^*\cdot(c^*+d)+b^*\cdot(c+d^*) = (a^*\cdot d+b^*\cdot c)+(a^*\cdot c^*+b^*\cdot d^*)
\end{aligned}$$<br>
故 $\lbrack (a^*\cdot c+b^*\cdot d,a^*\cdot d+b^*\cdot c) \rbrack=\lbrack (a^*\cdot c^*+b^*\cdot d^*,a^*\cdot d^*+b^*\cdot c^*) \rbrack$ ；<br>
所以 $\lbrack (a\cdot c+b\cdot d,a\cdot d+b\cdot c) \rbrack=\lbrack (a^*\cdot c^*+b^*\cdot d^*,a^*\cdot d^*+b^*\cdot c^*) \rbrack$ .<br>
(3) 若 $a+d\leq b+c$ ，则可设 $a+d+u=b+c$ ，所以
$$\begin{aligned}
(a^*+d^*+u)+(b+c) &= (a^*+b)+(c+d^*)+u = (a+b^*)+(c^*+d)+u \\
&= (a+d+u)+(b^*+c^*) = (b+c)+(b^*+c^*) = (b^*+c^*)+(b+c).
\end{aligned}$$<br>
根据命题 3.3 ，有 $a^*+d^*+u=b^*+c^*$ ，所以 $a^*+d^*\leq b^*+c^*$ .<br>
同理，若 $a^*+d^*\leq b^*+c^*$ ，则 $a+d\leq b+c$ .<br>
(4) 由于 $b+a^*=a^*+b=a+b^*=b^*+a$ ，故 $\lbrack (b,a) \rbrack=\lbrack (b^*,a^*) \rbrack$ . $\blacksquare$<br>
<br>
<b>命题 4.2</b>：$\mathbb{N}$ 可以按 $a\to\lbrack (a,0) \rbrack$ 嵌入 $\mathbb{Z}$ ，并保持加法、乘法、序.<br>
<b>证明</b>　只需要验证：<br>
① 若 $\lbrack (a,0) \rbrack=\lbrack (b,0) \rbrack$ ，则 $a=b$ ；<br>
② $\lbrack (a,0) \rbrack+\lbrack (b,0) \rbrack=\lbrack (a+b,0) \rbrack$；<br>
③ $\lbrack (a,0) \rbrack\cdot\lbrack (b,0) \rbrack=\lbrack (a\cdot b,0) \rbrack$；<br>
④ $a\leq b$ 当且仅当 $\lbrack (a,0) \rbrack\leq\lbrack (b,0) \rbrack$ .<br>
这四条都是显然的。 $\blacksquare$<br>
<br>
<b>命题 4.3</b>：$\mathbb{Z}$ 上的加法满足交换律、结合律；$\mathbb{Z}$ 上的乘法满足交换律、结合律、关于加法的分配律；$\mathbb{Z}$ 上的序仍是线性序.<br>
<b>证明</b>　直接利用定义并结合 $\mathbb{N}$ 上的相应性质即可。 $\blacksquare$<br>
<br>
<b>命题 4.4</b>：若整数 $p,q,r$ 满足 $p+r=q+r$ ，则 $p=q$ .<br>
<b>证明</b>　若 $\lbrack (a,b) \rbrack+\lbrack (e,f) \rbrack=\lbrack (c,d) \rbrack+\lbrack (e,f) \rbrack$ ，则 $\lbrack (a+e,b+f) \rbrack=\lbrack (c+e,d+f) \rbrack$ ，所以 $a+d+e+f=b+c+e+f$ ，从而根据命题 3.3 有 $a+d=b+c$ ，故 $\lbrack (a,b) \rbrack=\lbrack (c,d) \rbrack$ . $\blacksquare$<br>
<br>
<b>命题 4.5</b>：设 $p$ 是整数，若 $p\gt \lbrack (0,0) \rbrack$ ，则存在非零自然数 $a$ 使得 $p=\lbrack (a,0) \rbrack$ ；若 $p\lt \lbrack (0,0) \rbrack$ ，则存在非零自然数 $a$ 使得 $p=\lbrack (0,a) \rbrack$ .<br>
<b>证明</b>　(1) 若 $\lbrack (a,b) \rbrack\gt \lbrack (0,0) \rbrack$ ，则 $a+0\neq b+0$ ，$b+0\leq a+0$ ，从而 $b\lt a$ .<br>
这意味着存在自然数 $u$ 使得 $b+u=a=a+0$ ，故 $\lbrack (a,b) \rbrack=\lbrack (u,0) \rbrack$ .　显然 $u\neq 0$ ，否则 $a=b+u=b$ .<br>
(2) 若 $\lbrack (a,b) \rbrack\lt \lbrack (0,0) \rbrack$，则 $a+0\neq b+0$ ，$a+0\leq b+0$ ，从而 $a\lt b$ .<br>
这意味着存在自然数 $u$ 使得 $a+u=b=b+0$ ，故 $\lbrack (a,b) \rbrack=\lbrack (0,u) \rbrack$ .　显然 $u\neq 0$ ，否则 $a=a+u=b$ . $\blacksquare$<br>
<br>
<b>称大于 $\lbrack (0,0) \rbrack$ 的整数是正整数，小于 $\lbrack (0,0) \rbrack$ 的整数是负整数，而 $\lbrack (0,0) \rbrack$ 作为整数亦称为零.</b><br>
<br>
<b>命题 4.6</b>：正整数、负整数、零彼此不相等.<br>
<b>证明</b>　若非零自然数 $a$ 满足 $\lbrack (a,0) \rbrack=\lbrack (0,0) \rbrack$ ，则 $a+0=0+0$ ，从而 $a=0$ ，矛盾；<br>
若非零自然数 $a$ 满足 $\lbrack (0,a) \rbrack=\lbrack (0,0) \rbrack$ ，则 $0+0=a+0$ ，从而 $a=0$ ，矛盾；<br>
若非零自然数 $a,b$ 满足 $\lbrack (a,0) \rbrack=\lbrack (0,b) \rbrack$ ，则 $a+b=0+0=0$ ，从而根据命题 3.1 有 $a=b=0$ ，矛盾； $\blacksquare$<br>
<br>
<b>命题 4.7</b>：每个整数和自己相反数的和为零.<br>
<b>证明</b>　$\lbrack (a,b) \rbrack+\lbrack (b,a) \rbrack=\lbrack (a+b,b+a) \rbrack=\lbrack (a+b,a+b) \rbrack=\lbrack (0,0) \rbrack$ . $\blacksquare$<br>
<br>
将整数 $p$ 的相反数记为 $-p$ ，那么可以定义 $\mathbb{Z}$ 上的减法：$p-q=p+(-q)$ .<br>
也就是说，减去一个数，其实就是加上这个数的相反数。<br>
于是我们马上就有「移项」：若 $p+q=r$ ，则 $p=p+q+(-q)=r+(-q)=r-q$ .<br>
<br>
<b>命题 4.8</b>：若两整数 $p,q$ 的乘积 $p\cdot q=\lbrack (0,0) \rbrack$ ，则 $p=\lbrack (0,0) \rbrack$ 或 $q=\lbrack (0,0) \rbrack$ .<br>
<b>证明</b>　假设结论不成立，若 $p,q$ 都是正整数 ，则可设 $p=\lbrack (a,0) \rbrack$ ，$q=\lbrack (b,0) \rbrack$ ，这里 $a,b$ 是非零自然数.<br>
那么 $\lbrack (0,0) \rbrack=p\cdot q=\lbrack (a,0) \rbrack\cdot\lbrack (b,0) \rbrack=\lbrack (a\cdot b,0) \rbrack$ ，从而 $a\cdot b+0=0+0$ ，即 $a\cdot b=0$ ，根据命题 3.9 ，这得到 $a=0$ 或 $b=0$ ，矛盾.<br>
<br>
若 $p,q$ 都是负整数 ，则可设 $p=\lbrack (0,a) \rbrack$ ，$q=\lbrack (0,b) \rbrack$ ，这里 $a,b$ 是非零自然数.<br>
那么 $\lbrack (0,0) \rbrack=p\cdot q=\lbrack (0,a) \rbrack\cdot\lbrack (0,b) \rbrack=\lbrack (a\cdot b,0) \rbrack$ ，从而 $0+a\cdot b=0+0$ ，即 $a\cdot b=0$ ，根据命题 3.9 ，这得到 $a=0$ 或 $b=0$ ，矛盾.<br>
<br>
若 $p$ 是正整数 ，$q$ 是负整数 ，则可设 $p=\lbrack (a,0) \rbrack$ ，$q=\lbrack (0,b) \rbrack$ ，这里 $a,b$ 是非零自然数.<br>
那么 $\lbrack (0,0) \rbrack=p\cdot q=\lbrack (a,0) \rbrack\cdot\lbrack (0,b) \rbrack=\lbrack (0,a\cdot b) \rbrack$ ，从而 $0+0=0+a\cdot b$ ，即 $a\cdot b=0$ ，根据命题 3.9 ，这得到 $a=0$ 或 $b=0$ ，矛盾.<br>
<br>
这就表明 $p=\lbrack (0,0) \rbrack$ 或 $q=\lbrack (0,0) \rbrack$ . $\blacksquare$<br>
<br>
<b>命题 4.9</b>：两正整数或两负整数的乘积为正整数，正整数和负整数的乘积为负整数，零和任何整数的乘积为零.<br>
直接验证即可。 $\blacksquare$<br>
<br>
<b>命题 4.10</b>：对整数 $p,q,r$，$p\geq q$ 当且仅当 $p+r\geq q+r$，$p\gt q$ 当且仅当 $p+r\gt q+r$ ，特别地可以取 $r=-q$ ，得到 $p\geq q$ 当且仅当 $p-q\geq\lbrack (0,0) \rbrack$ ，$p\gt q$ 当且仅当 $p-q\geq\lbrack (0,0) \rbrack$ .<br>
比较简单，无需赘述。 $\blacksquare$<br>
<br>
<i>该结论可以推出：和某个整数 $p$ 相加为零的整数 $q$ 是唯一的，且 $q$ 就是 $p$ 相反数。这也将作为命题 4.10 的一部分被后文引用。</i><br>
<br>
<b>命题 4.11</b>：对整数 $p,q,r$，若 $r$ 是正整数，则 $p\cdot r\geq q\cdot r$ 当且仅当 $p\geq q$ ，$p\cdot r\gt q\cdot r$ 当且仅当 $p\gt q$ ；若 $r$ 是负整数，则 $p\cdot r\geq q\cdot r$ 当且仅当 $p\leq q$ ，$p\cdot r\gt q\cdot r$ 当且仅当 $p\lt q$ .<br>
也比较简单。 $\blacksquare$<br>
<br>
<i>该结论可以推出：若 $r\neq 0$ ，$p\cdot r=q\cdot r$ ，则 $p=q$ .　这也将作为命题 4.11 的一部分被后文引用。</i><br>
<br>
<b>命题 4.12</b>：设 $p$ 是整数，那么不存在整数 $q$ ，使得 $p\lt q$ ，且 $q\lt p+\lbrack (0',0) \rbrack$ .<br>
<b>证明</b>　假设 $p\lt q$ ，$q\lt p+\lbrack (0',0) \rbrack$ .<br>
设 $p=\lbrack (a,b) \rbrack$ ，$q=\lbrack (c,d) \rbrack$ ，则 $\lbrack (a,b) \rbrack\lt \lbrack (c,d) \rbrack$ ，$\lbrack (c,d) \rbrack\lt \lbrack (a,b) \rbrack+\lbrack (0',0) \rbrack=\lbrack (a+0',b) \rbrack$ .<br>
从而 $a+d\lt b+c$ ，$b+c\lt a+d+0'$ ，这和命题 3.10 矛盾。<br>
所以命题 4.12 得证。 $\blacksquare$<br>
<br>
<b>命题 4.13</b>：设 $p$ 是整数 ，则 $-(-p)=p$ .<br>
<b>证明</b>　设 $p=\lbrack (a,b) \rbrack$ ，则 $-p=\lbrack (b,a) \rbrack$ ，所以 $-(-p)=-\lbrack (b,a) \rbrack=\lbrack (a,b) \rbrack=p$ . $\blacksquare$<br>
<br>
<b>命题 4.14</b>：设 $p,q$ 是整数 ，则 $(-p)\cdot q=-(p\cdot q)=p\cdot(-q)$ ，$(-p)\cdot(-q)=p\cdot q$ .<br>
<b>证明</b>　由于 $p\cdot q+(-p)\cdot q=(p+(-p))\cdot q=0\cdot q=0$ ，故 $(-p)\cdot q=-(p\cdot q)$ ；<br>
由于 $p\cdot(-q)+p\cdot q=p\cdot((-q)+q)=p\cdot 0=0$ ，故 $p\cdot(-q)=-(p\cdot q)$ .<br>
从而 $(-p)\cdot(-q)=-(p\cdot(-q))=-(-(p\cdot q))=p\cdot q$ ，最后一步使用命题 4.13 . $\blacksquare$<br>
<br>
<b>命题 4.15</b>：设 $p$ 是整数 ，则 $p\cdot\lbrack (0',0) \rbrack=p$ ，$p\cdot\lbrack (0,0') \rbrack=-p$ .<br>
<b>证明</b>　设 $p=\lbrack (a,b) \rbrack$ ，则根据整数乘法定义就有 $\lbrack (a,b) \rbrack\cdot\lbrack (0',0) \rbrack=\lbrack (a\cdot 0',b\cdot 0') \rbrack$ ，$\lbrack (a,b) \rbrack\cdot\lbrack (0,0') \rbrack=\lbrack (b\cdot 0',a\cdot 0') \rbrack$ .<br>
结合命题 2.5 可知 $\lbrack (a,b) \rbrack\cdot\lbrack (0',0) \rbrack=\lbrack (a\cdot 0',b\cdot 0') \rbrack=\lbrack (a,b) \rbrack$ ，$\lbrack (a,b) \rbrack\cdot\lbrack (0,0') \rbrack=\lbrack (b\cdot 0',a\cdot 0') \rbrack=\lbrack (b,a) \rbrack=-\lbrack (a,b) \rbrack$ . $\blacksquare$<br>
<br>
<b>命题 4.16</b>：若 $\mathbb{Z}$ 的一个非空子集有上界，则必有最大数；若 $\mathbb{Z}$ 的一个非空子集有下界，则必有最小数.<br>
<b>证明</b>　直接根据命题 3.8 即可得到。 $\blacksquare$<br>
<br>
目前的结论已经能够推出 $\mathbb{Z}$ 是一个整环，此时就可以引入各种整环上的概念，以及很多初等数论知识。<br>
<br>
<b>我们只提出一个性质：整除。</b><br>
<br>
若整数 $p,q$ 满足：存在整数 $r$ 使得 $p\cdot r=q$ ，则称 $p$ <b>整除</b> $q$ ，可记为 $p|q$ ，此时称 $q$ 是 $p$ 的<b>倍数</b>，$p$ 是 $q$ 的<b>约数或因数</b>。<br>
对整数 $p$ ，设 $\operatorname{abs}(p)$ 为 $p$ 的<b>绝对值</b>：若 $p\geq\lbrack (0,0) \rbrack$ ，则规定 $\operatorname{abs}(p)=p$ ；否则规定 $\operatorname{abs}(p)=-p$ .　显然，$\operatorname{abs}(p)\geq\lbrack (0,0) \rbrack$ .<br>
整数 $p$ 的绝对值也记作 $|p|$ ，即 $|p|=\operatorname{abs}(p)$ .<br>
<br>
<b>命题 4.17</b>：对整数 $p,q$，四个结论 $p|q$ ，$(-p)|q$ ，$p|(-q)$ ，$(-p)|(-q)$ 两两等价.<br>
显然成立。 $\blacksquare$<br>
<br>
<b>命题 4.18</b>：若整数 $p,q$ 都不为 $\lbrack (0,0) \rbrack$ ，且 $p|q$ ，则 $\operatorname{abs}(p)\leq\operatorname{abs}(q)$ .<br>
<b>证明</b>　根据命题 4.17 ，不妨设 $p,q$ 都是正整数.<br>
由于 $p|q$ ，可设 $p\cdot r=q$ ，根据命题 4.9 有 $r\gt \lbrack (0,0) \rbrack$ ，所以 $r\geq\lbrack (0,0) \rbrack+\lbrack (0',0) \rbrack=\lbrack (0',0) \rbrack$ ，故根据命题 4.11 和 4.15 有 $q=p\cdot r\geq p\cdot\lbrack (0',0) \rbrack=p$ . $\blacksquare$<br>
<br>
<b>命题 4.19</b>：若整数 $p,q$ 不全为 $\lbrack (0,0) \rbrack$ ，则存在一个最大的正整数 $d$ ，它同时整除 $p$ 和 $q$ ，这称为 $p$ 和 $q$ 的最大公因数，记为 $\gcd(p,q)$ .<br>
<b>证明</b>　首先，若整数 $p,q$ 不全为 $\lbrack (0,0) \rbrack$ ，则所有整除 $p$ 和 $q$ 的正整数包括 $\lbrack (0',0) \rbrack$ .<br>
另一方面，根据命题 4.18 以及 $p,q$ 不全为 $\lbrack (0,0) \rbrack$ 可知：所有整除 $p$ 和 $q$ 的正整数一定不超过 $\operatorname{abs}(p)$ , $\operatorname{abs}(q)$ 的较大值。<br>
从而根据命题 4.16 ，$p,q$ 存在一个最大的公因数。 $\blacksquare$<br>
<br>
<i>整数 $p$ 和 $q$ 的最大公因数记为 $\gcd(p,q)$ .</i><br>
<br>
<b>命题 4.20</b>：设 $p$ 是整数，则 $\gcd(p,\lbrack (0',0) \rbrack)=\lbrack (0',0) \rbrack$ ；同时若 $p\neq\lbrack (0,0) \rbrack$ ，则 $\gcd(p,\lbrack (0,0) \rbrack)=\gcd(p,p)=\operatorname{abs}(p)$ .<br>
比较显然，略过。 $\blacksquare$<br>
<br>
<b>命题 4.21</b>：设 $p,q$ 是整数，且 $\gcd(p,q)=\lbrack (0',0) \rbrack$ ，则存在整数 $r,s$ ，使得 $p\cdot r+q\cdot s=\lbrack (0',0) \rbrack$ .<br>
<b>证明</b>　如果 $q=\lbrack (0,0) \rbrack$ ，则根据 $\gcd(p,\lbrack (0,0) \rbrack)=\lbrack (0',0) \rbrack$ ，根据命题 4.20 ，有 $\operatorname{abs}(p)=\lbrack (0',0) \rbrack$ ，故根据 $p\cdot p=p\cdot p+q\cdot\lbrack (0,0) \rbrack=\lbrack (0',0) \rbrack$ 可知结论成立；<br>
如果 $p=\lbrack (0,0) \rbrack$，同理可证结论成立；<br>
<br>
下面考虑 $p,q$ 都是整数的情形。根据命题 4.14 ，又可以不妨设 $p,q$ 都是正整数：<br>
对无序正整数对 $\{a,b\}$ ，若 $a\lt b$ ，则可以将 $\{a,b\}$ 改为 $\{a,b-a\}$ ；若 $a\gt b$ ，则可以将 $\{a,b\}$ 改为 $\{a-b,b\}$ .<br>
每当一个不相等的无序正整数对进行一次这样的操作后，两个数中的较大一个一定变得更小。<br>
将所有经过有限次操作得到的数对的较大数构成的集合记为 $L$ ，则根据命题 4.16 ，集合 $L$ 存在最小元素 $d$ .<br>
所以无序正整数对 $\{p,q\}$ 能通过有限次操作至较大数为 $d$ 的时刻，此时根据 $d$ 的最小性，数对无法继续操作，从而必然两数相等。<br>
<br>
显然，整数 $d$ 整除 $a$ 和 $b$ 等价于 $d$ 整除 $a$ 和 $b-a$ ，也等价于 $d$ 整除 $a-b$ 和 $b$ .<br>
所以每次操作后，两数的最大公因数保持不变，从而根据命题 4.20 ，可知 $\lbrack (0',0) \rbrack=\gcd(p,q)=\gcd(d,d)=\operatorname{abs}(d)=d$ .<br>
<br>
设 $T=\{ (x,y)\in \mathbb{Z}\times \mathbb{Z} \mid \text{存在 } u,v\in \mathbb{Z} \text{ ，使得 } x\cdot u+y\cdot v=\lbrack (0',0) \rbrack \}$ .<br>
<br>
由于将 $\{a,b\}$ 操作为 $\{a-b,b\}$ 后，如果 $(a-b)\cdot k+b\cdot k^*=\lbrack (0',0) \rbrack$ ，则 $a\cdot k+b\cdot(k^*-k)=\lbrack (0',0) \rbrack$ ；<br>
将 $\{a,b\}$ 操作为 $\{a,b-a\}$ 后，如果 $a\cdot k+(b-a)\cdot k^*=\lbrack (0',0) \rbrack$ ，则 $a\cdot(k-k^*)+b\cdot k^*=\lbrack (0',0) \rbrack$ .<br>
故可以得到：若 $(a-b,b)\in T$ 或 $(a,b-a)\in T$ ，则 $(a,b)\in T$ .<br>
<br>
再根据 $d\cdot\lbrack (0',0) \rbrack+d\cdot\lbrack (0,0) \rbrack=d=\lbrack (0',0) \rbrack$ 可得 $(d,d)\in T$ ，就可以反推得到 $(p,q)\in T$ ，结论得证。 $\blacksquare$<br>
<br>
<b>命题 4.22</b>：设 $p,q,r$ 是整数，且 $\gcd(p,q)=\lbrack (0',0) \rbrack$ ，同时 $p|(q\cdot r)$ ，则 $p|r$ .<br>
<b>证明</b>　根据命题 4.21 ，存在整数 $u,v$ ，使得 $p\cdot u+q\cdot v=\lbrack (0',0) \rbrack$ ，所以 $p\cdot(u\cdot r)+(q\cdot r)\cdot v=\lbrack (0',0) \rbrack\cdot r=r$ .<br>
而 $p|(q\cdot r)$ ，所以 $p|(p\cdot(u\cdot r)+(q\cdot r)\cdot v)$ ，从而 $p|r$ ，结论得证。 $\blacksquare$<br>

<br><br>


## 第五章  有理数<br>
<br>
再由整数定义有理数：<br>
<br>
在 $\mathbb{Z}\times (\mathbb{Z}\setminus\{\lbrack (0,0) \rbrack\})$ 上定义如下等价关系：如果整数 $p,q,r,s$ 满足：$p\cdot s=q\cdot r$ ，则称 $(p,q)\sim(r,s)$ .<br>
下面证明这确实是等价关系。<br>
①反身性：由于 $p\cdot q=p\cdot q$ ，故 $(p,q)\sim(p,q)$ ；<br>
②对称性：若 $(p,q)\sim(r,s)$ ，则 $p\cdot s=q\cdot r$ ，所以 $q\cdot r=p\cdot s$ ，故 $(r,s)\sim(p,q)$ .<br>
③传递性：若 $(p,q)\sim(r,s)$ ，$(r,s)\sim(u,v)$ ，则 $p\cdot s=q\cdot r$ ，$r\cdot v=s\cdot u$，故 $(p\cdot v)\cdot(r\cdot s)=(p\cdot s)\cdot(r\cdot v)=(q\cdot r)\cdot(s\cdot u)=(q\cdot u)\cdot(r\cdot s)$ .　若 $r\neq\lbrack (0,0) \rbrack$ ，则根据命题 4.11 有 $p\cdot v=q\cdot u$ ，所以 $(p,q)\sim(u,v)$ ；若 $r=\lbrack (0,0) \rbrack$ ，则 $p\cdot s=s\cdot u=\lbrack (0,0) \rbrack$ ，但 $s\neq\lbrack (0,0) \rbrack$ ，所以 $p=u=\lbrack (0,0) \rbrack$ ，从而 $p\cdot v=\lbrack (0,0) \rbrack=q\cdot u$ ，所以 $(p,q)\sim(u,v)$ .<br>
<br>
在这样的等价关系下，全体等价类构成的集合定义为有理数集 $\mathbb{Q}$ ，每个等价类是一个有理数。将 $(p,q)$ 所在的等价类记为 $\left\langle \frac{p}{q} \right\rangle$ .<br>
下面将整数上的加法、乘法和序迁移过来。<br>
<br>
定义加法为：$\left\langle \frac{p}{q} \right\rangle+\left\langle \frac{r}{s} \right\rangle=\left\langle \frac{p\cdot s+q\cdot r}{q\cdot s} \right\rangle$ ；<br>
定义乘法为：$\left\langle \frac{p}{q} \right\rangle\cdot\left\langle \frac{r}{s} \right\rangle=\left\langle \frac{p\cdot r}{q\cdot s} \right\rangle$ ；<br>
定义序为：若 $\left\langle \frac{p}{q} \right\rangle$ , $\left\langle \frac{r}{s} \right\rangle$ 满足 $q\cdot s\cdot(p\cdot s)\leq q\cdot s\cdot(q\cdot r)$ ，则规定 $\left\langle \frac{p}{q} \right\rangle\leq\left\langle \frac{r}{s} \right\rangle$ .<br>
定义相反数：$\left\langle \frac{p}{q} \right\rangle$ 的相反数是 $\left\langle \frac{-p}{q} \right\rangle$ ，也记为 $-\left\langle \frac{p}{q} \right\rangle$ .<br>
再同时定义倒数：若 $\left\langle \frac{p}{q} \right\rangle\neq\left\langle \frac{0}{0'} \right\rangle$（此即 $p\neq 0$ ），则称 $\left\langle \frac{p}{q} \right\rangle$ 的倒数是 $\left\langle \frac{q}{p} \right\rangle$ ，记为 $\left\langle \frac{p}{q} \right\rangle^{-1} = \left\langle \frac{q}{p} \right\rangle$ .<br>
<br>
由于很多性质的证明都和整数类似，下面的命题 5.1 至 5.5 就直接给出内容了，证明反正也不难（<br>
<br>
<b>命题 5.1</b>：$\mathbb{Q}$ 上的加法、乘法、序、相反数、倒数都是良定义的.<br>
<br>
<b>命题 5.2</b>：$\mathbb{Z}$ 可以按 $p\to\left\langle \frac{p}{0'} \right\rangle$ 嵌入 $\mathbb{Q}$ ，并保持加法、相反数、乘法、序.<br>
<br>
<b>命题 5.3</b>：$\mathbb{Q}$ 关于其上的加法和乘法运算，以及零元 $\left\langle \frac{0}{0'} \right\rangle$ 和幺元 $\left\langle \frac{0'}{0'} \right\rangle$ 构成一个域，具体来说：<br>
① $\mathbb{Q}$ 上加法满足交换律和结合律；<br>
② 对任意 $x\in\mathbb{Q}$ ，有 $x+\left\langle \frac{0}{0'} \right\rangle=x$ ；<br>
③ 对任意 $x\in\mathbb{Q}$ ，存在唯一的 $y\in\mathbb{Q}$ ，使得 $x+y=\left\langle \frac{0}{0'} \right\rangle$ ，且这里的 $y$ 是 $x$ 的相反数；<br>
④ $\mathbb{Q}$ 上乘法满足交换律、结合律，以及关于加法的分配律；<br>
⑤ $\left\langle \frac{0'}{0'} \right\rangle\neq\left\langle \frac{0}{0'} \right\rangle$ ，且对任意 $x\in\mathbb{Q}$ ，有 $x\cdot\left\langle \frac{0'}{0'} \right\rangle=x$ ；<br>
⑥ 对任意 $x\in\mathbb{Q}\setminus\{\left\langle \frac{0}{0'} \right\rangle\}$ ，存在唯一的 $y\in\mathbb{Q}$ ，使得 $x\cdot y=\left\langle \frac{0'}{0'} \right\rangle$ ，且这里的 $y$ 是 $x$ 的倒数.<br>
<br>
<i>当 $\mathbb{Q}$ 作为域时，有一些性质，例如：</i><br>
<i>① $x\cdot\left\langle \frac{0}{0'} \right\rangle=\left\langle \frac{0}{0'} \right\rangle$ ；</i><br>
<i>② 若 $x\cdot y=\left\langle \frac{0}{0'} \right\rangle$ ，则 $x=\left\langle \frac{0}{0'} \right\rangle$ 或 $y=\left\langle \frac{0}{0'} \right\rangle$ .</i><br>
<br>
<b>命题 5.4</b>：$\mathbb{Q}$ 关于 $\leq$ 构成线性序集，即对任意 $x,y\in\mathbb{Q}$ ，有 $x\leq y$ 或 $y\leq x$ ，也即对任意 $x,y\in\mathbb{Q}$ ，有 $x\lt y$ ，$x=y$ ，$x\gt y$ 三者恰成立其一。<br>
<br>
<b>命题 5.5</b>：$\mathbb{Q}$ 上的加法和乘法运算关于序 $\leq$ 有一些熟知的性质，如<br>
<b>① 对 $x,y,z\in\mathbb{Q}$ ，有 $x\leq y$ 当且仅当 $x+z\leq y+z$ ，同时 $x\lt y$ 当且仅当 $x+z\lt y+z$ ；</b><br>
<b>② 对 $x,y\in\mathbb{Q}$ ，有 $x\cdot y\gt\left\langle \frac{0}{0'} \right\rangle$ 当且仅当 $x,y\gt\left\langle \frac{0}{0'} \right\rangle$ 或 $x,y\lt\left\langle \frac{0}{0'} \right\rangle$ ，同时 $x\cdot y\lt\left\langle \frac{0}{0'} \right\rangle$ 当且仅当 $x\lt\left\langle \frac{0}{0'} \right\rangle\lt y$ 或 $y\lt\left\langle \frac{0}{0'} \right\rangle\lt x$ ；</b><br>
<b>③ 对 $x,y,z\in\mathbb{Q}$ ，若 $z\gt\left\langle \frac{0}{0'} \right\rangle$ ，则 $x\leq y$ 当且仅当 $x\cdot z\leq y\cdot z$ ，且有 $x\lt y$ 当且仅当 $x\cdot z\lt y\cdot z$ ；若 $z\lt\left\langle \frac{0}{0'} \right\rangle$ ，则 $x\leq y$ 当且仅当 $x\cdot z\geq y\cdot z$ ，且有 $x\lt y$ 当且仅当 $x\cdot z\gt y\cdot z$ ；</b><br>
<b>④ $\left\langle \frac{0'}{0'} \right\rangle\gt\left\langle \frac{0}{0'} \right\rangle$ .</b><br>
<br>
<b>命题 5.6</b>：对任意有理数 $x$ ，存在唯一的整数组 $p,q$ ，满足 $q\gt\lbrack (0,0) \rbrack$ ，$x=\left\langle \frac{p}{q} \right\rangle$ ，且 $\gcd(p,q)=\lbrack (0',0) \rbrack$ .<br>
<b>证明</b>　我们可以考虑 $\mathbb{Z}$ 的如下子集：$L=\{ q \mid q\gt\lbrack (0,0) \rbrack \text{ ，且存在整数 } p \text{ ，使得 } x=\left\langle \frac{p}{q} \right\rangle \}$ .<br>
<br>
设 $x=\left\langle \frac{r}{s} \right\rangle=\left\langle \frac{-r}{-s} \right\rangle$ ，则 $s$ 和 $-s$ 中必有一个正整数，从而 $L$ 非空.<br>
由于 $\lbrack (0,0) \rbrack$ 显然是 $L$ 的下界，故根据命题 4.16 ，集合 $L$ 一定存在最小元素，记最小元素为 $q$ .<br>
那么 $q\gt\lbrack (0,0) \rbrack$ ，且存在整数 $p$ ，使得 $x=\left\langle \frac{p}{q} \right\rangle$.<br>
由于 $p$ 和 $q$ 不全为 $\lbrack (0,0) \rbrack$ ，根据命题 4.17 ，可设正整数 $d=\gcd(p,q)$ .<br>
——假设 $d\gt\lbrack (0',0) \rbrack$ ，根据 $d$ 整除 $p$ 和 $q$ ，设整数 $p^*,q^*$ 满足 $p=d\cdot p^*$ ，$q=d\cdot q^*$ ，容易验证 $\left\langle \frac{p}{q} \right\rangle=\left\langle \frac{p^*}{q^*} \right\rangle$ .<br>
——根据命题 4.9 ，以及 $d$ 和 $q$ 都是正整数，可得 $q^*$ 是正整数，所以根据 $x=\left\langle \frac{p^*}{q^*} \right\rangle$ 可得 $q^*\in L$ .<br>
——但由于 $d\gt\lbrack (0',0) \rbrack$ ，根据命题 4.11 和 4.15 可得 $q=d\cdot q^*\gt\lbrack (0',0) \rbrack\cdot q^*=q^*$ ，这表明 $L$ 中还有一个比 $q$ 更小的元素 $q^*$ ，这和 $q$ 是最小元素矛盾。<br>
——从而假设不成立。<br>
故根据上面的反证法，可知 $d=\lbrack (0',0) \rbrack$ ，所以 $p,q$ 是满足条件的整数组。<br>
<br>
如果还存在另一组整数 $r,s$ ，使得 $s\gt\lbrack (0,0) \rbrack$ ，$x=\left\langle \frac{r}{s} \right\rangle$ ，且 $\gcd(r,s)=\lbrack (0',0) \rbrack$ .<br>
那么根据 $\left\langle \frac{p}{q} \right\rangle=x=\left\langle \frac{r}{s} \right\rangle$ ，可知 $p\cdot s=r\cdot q$ .<br>
由 $p\cdot s=r\cdot q$ 可得 $q|(p\cdot s)$ ，而 $\gcd(p,q)=\lbrack (0',0) \rbrack$ ，故根据命题 4.22 ，有 $q|s$ .<br>
由 $p\cdot s=r\cdot q$ 可得 $s|(r\cdot q)$ ，而 $\gcd(r,s)=\lbrack (0',0) \rbrack$ ，故根据命题 4.22 ，有 $s|q$ .<br>
结合 $s,q$ 是正整数，根据命题 4.18 ，就得到 $q\leq s$ 且 $s\leq q$ ，所以 $q=s\gt\lbrack (0',0) \rbrack$ .<br>
根据 $p\cdot s=r\cdot q$ 和命题 4.11 ，即可得到 $p=r$ .<br>
这就说明 $p=r$ ，$q=s$ ，所以满足条件的整数组是唯一的。 $\blacksquare$<br>
<br>
<b>至此，我们得到每个有理数都有唯一的既约表示 $\left\langle \frac{p}{q} \right\rangle$ ，满足 $q\gt\lbrack (0,0) \rbrack$ ，且 $\gcd(p,q)=\lbrack (0',0) \rbrack$ .</b><br>
<br>
<b>命题 5.7</b>：设 $p,q,r,s$ 是整数，$q,s$ 是正整数，那么 $\left\langle \frac{p}{q} \right\rangle\gt\left\langle \frac{r}{s} \right\rangle$ 当且仅当 $p\cdot s\gt r\cdot q$ ， $\left\langle \frac{p}{q} \right\rangle\geq\left\langle \frac{r}{s} \right\rangle$ 当且仅当 $p\cdot s\geq r\cdot q$ .<br>
证明应该不难。 $\blacksquare$<br>
<br>
<b>命题 5.8</b>：设 $p,q$ 是整数 ，若 $q\gt\lbrack (0,0) \rbrack$ ，则 $\left\langle \frac{p}{q} \right\rangle$ 和 $\left\langle \frac{0}{0'} \right\rangle$ 的大小关系就是 $p$ 和 $\lbrack (0,0) \rbrack$ 的大小关系；若 $q\lt\lbrack (0,0) \rbrack$ ，则 $\left\langle \frac{p}{q} \right\rangle$ 和 $\left\langle \frac{0}{0'} \right\rangle$ 的大小关系和 $p$ 和 $\lbrack (0,0) \rbrack$ 的大小关系刚好相反.<br>
证明应该也不难。 $\blacksquare$<br>
<br>
<b>命题 5.9</b>：对任意有理数 $x,y$ ，若 $x\lt y$ ，则存在有理数 $z$ ，使得 $x\lt z\lt y$ .<br>
<b>证明</b>　(1) 若 $x\lt\left\langle \frac{0}{0'} \right\rangle\lt y$，可直接取 $z=\left\langle \frac{0'}{0'} \right\rangle$ .<br>
(2) 若 $\left\langle \frac{0}{0'} \right\rangle\leq x\lt y$，设 $x=\left\langle \frac{p}{q} \right\rangle$ ，$y=\left\langle \frac{r}{s} \right\rangle$ ，且确保 $q,s$ 都是正整数，则根据命题 5.8 ，可知 $p$ 是非负整数，$r$ 是正整数。<br>
取 $z=\left\langle \frac{p+r}{q+s} \right\rangle$ ，则根据 $q+s\gt q+\lbrack (0,0) \rbrack=q\gt\lbrack (0,0) \rbrack$ 可知 $q+s$ 是正整数。<br>
根据命题 5.7 ，可由 $x\lt y$ 得到 $p\cdot s\lt r\cdot q$ .<br>
从而 $p\cdot(q+s)=p\cdot q+p\cdot s\lt p\cdot q+r\cdot q=(p+r)\cdot q$ ，且 $(p+r)\cdot s=p\cdot s+r\cdot s\lt r\cdot q+r\cdot s=r\cdot(q+s)$ ，所以 $x\lt z\lt y$ .<br>
(3) 若 $x\lt y\leq\left\langle \frac{0}{0'} \right\rangle$ ，则 $\left\langle \frac{0}{0'} \right\rangle\leq-y\lt-x$ ，根据 (2) 的证明，存在有理数 $z^*$ ，使得 $-y\lt z^*\lt-x$ ，所以 $x\lt-z^*\lt y$ . $\blacksquare$<br>
<br>
<i>注：也可以直接取 $z=(x+y)\cdot\left\langle \frac{0'}{0''} \right\rangle$ .</i><br>
<br>
以上的内容基本上说明了：$\mathbb{Q}$ 是一个域，而且带有相应的序关系。<br>
<br>
同时，$\mathbb{Q}$ 上的元素有唯一的既约表示，同时任何两个有理数之间都有新的有理数。<br>
<br>
有理数集 $\mathbb{Q}$ 还有一个较为重要的性质就是：不完备。以下面的例子说明：<br>
<br>
<b>练习 5.10</b>：定义 $\mathbb{Q}$ 的子集 $L=\{ x\in\mathbb{Q} \mid x\lt\left\langle \frac{0}{0'} \right\rangle \text{ 或 } x\cdot x\lt\left\langle \frac{0''}{0'} \right\rangle \}$ ，则有如下结论：<br>
① 对任意 $x,y\in\mathbb{Q}$ ，若 $x\lt y$ ，$y\in L$ ，则 $x\in L$ ；<br>
② 对任意 $x\in L$ ，存在 $y\in L$ ，使得 $x\lt y$ ；<br>
③ 对任意 $x\in\mathbb{Q}\setminus L$ ，存在 $y\in\mathbb{Q}\setminus L$ ，使得 $y\lt x$ .<br>
证明留给感兴趣的朋友们（（<br>
<br>
这个结论表明 $L$ 是 $\mathbb{Q}$ 的一个无理分划。在引入实数后，可以看出这反映的就是实数上“根号二”的无理性。<br>
<br><br>
最后我们准备定义实数。作如下准备：<br>
<br>
1.　由于自然数可以嵌入整数，整数可以嵌入有理数，故我们直接视它们有子集关系。以后的书写不再那么形式化；<br>
<br>
2.　我们把 $0'$ 记为 $1$ ，$0''$ 记为 $2$ ，以此类推。不过它们只代表有限次后继数，和进制表示暂时无关；<br>
<br>
3.　若 $p,q$ 是有理数，$q$ 非零，那么除法运算写作 $p/q$ ，除以一个数就是乘以这个数的倒数。亦可以直接理解为：$p/q=p\cdot q^{-1}$ .<br>

<br><br>


## 第六章  实数<br>
<br>
我们首先考虑有理数列。<br>
<br>
每个有理数列是从自然数集 $\mathbb{N}$ 到 $\mathbb{Q}$ 的一个映射。<br>
<br>
例如我们记 $\{q_\cdot\}$ 代表映射 $q : \mathbb{N}\to\mathbb{Q}$ ，称 $\{q_\cdot\}$ 为一个有理数列。<br>
<br>
然后定义<b>基本列</b>。设 $\{q_\cdot\}$ 是有理数列：<br>
若对任意 $c\in\mathbb{Q}^+$（$\mathbb{Q}^+$指的是正有理数集），都存在自然数 $N$ ，使得对任意自然数 $m,n\gt N$ ，有 $\operatorname{abs}(q_m-q_n)\lt c$ .<br>
则称 $\{q_\cdot\}$ 是一个<b>有理数基本列</b>。<br>
<br>
全体有理数基本列里可以定义如下等价关系：<br>
设 $\{p_\cdot\}$ 和 $\{q_\cdot\}$ 是两个有理数基本列.<br>
若对任意 $c\in\mathbb{Q}^+$ ，都存在自然数 $N$ ，使得对任意自然数 $n\gt N$ ，都有 $\operatorname{abs}(p_n-q_n)\lt c$ .<br>
则称两个有理数基本列 $\{p_\cdot\}$ 和 $\{q_\cdot\}$ 等价，即 $\{p_\cdot\}\sim\{q_\cdot\}$ .<br>
<br>
在这样的等价关系下，全体有理数基本列构成的全体等价类定义为<b>实数集 $\mathbb{R}$</b> ，每个等价类是一个实数.<br>
若 $\{p_\cdot\}$ 是有理数基本列，记该有理数基本列所在的等价类为 $\lbrack\{p_\cdot\}\rbrack$ .<br>
<br>
借助有理数 $\mathbb{Q}$ 上的对应结构，全体实数集上定义如下运算和序等：<br>
(1) $\lbrack\{p_\cdot\}\rbrack+\lbrack\{q_\cdot\}\rbrack=\lbrack\{p_\cdot+q_\cdot\}\rbrack$ ；<br>
(2) $\lbrack\{p_\cdot\}\rbrack$ 的相反数为 $\lbrack\{-p_\cdot\}\rbrack$ ；<br>
(3) $\lbrack\{p_\cdot\}\rbrack\cdot\lbrack\{q_\cdot\}\rbrack=\lbrack\{p_\cdot\cdot q_\cdot\}\rbrack$ ；<br>
(4) 若 $\lbrack\{p_\cdot\}\rbrack\neq\lbrack\{0\}\rbrack$（ $\lbrack\{0\}\rbrack$ 代表恒为 $0$ 的有理序列），则记 $k$ 是最小的，满足 $n\geq k$ 时都有 $p_n\neq 0$ 的自然数 $k$ ，则规定 $\lbrack\{p_\cdot\}\rbrack$ 的倒数为 $\lbrack\{q_\cdot\}\rbrack$ ，其中 $q_n=1/p_{n+k'}$ ；<br>
(5) 若对任意 $c\in\mathbb{Q}^+$ ，都存在自然数 $N$ ，使得 $n\gt N$ 时有 $p_n\leq q_n+c$ ，则规定 $\lbrack\{p_\cdot\}\rbrack\leq\lbrack\{q_\cdot\}\rbrack$ ；<br>
(6) 规定 $\lbrack\{p_\cdot\}\rbrack$ 的绝对值 $\operatorname{abs}(\lbrack\{p_\cdot\}\rbrack)$ 为 $\lbrack\{\operatorname{abs}(p_\cdot)\}\rbrack$ .<br>
<br>
<b>命题 6.1</b>：实数集 $\mathbb{R}$ 上的加法、乘法、相反数、倒数、序均良定义.<br>
<b>证明</b>　证明主要需要验证：<br>
①两个有理数基本列的和、乘积、绝对值都是有理数基本列；<br>
②恒为某个固定有理数的有理序列一定是有理数基本列；<br>
③每个有理数基本列的子列都和自身等价；<br>
④和 $\lbrack\{0\}\rbrack$ 不等价的有理数基本列至多有有限项为 $0$ ，故一定存在自然数 $k$ ，使得 $n\geq k$ 时都有 $p_n\neq 0$ .<br>
同时，存在 $c\in\mathbb{Q}^+$ ，使得 $n\geq k$ 时都有 $\operatorname{abs}(p_n)\gt c$ .<br>
⑤在验证结论时，可以设相应的 $c\in\mathbb{Q}^+$ 满足 $c\lt 1$ .<br>
<br>
具体细节省略。 $\blacksquare$<br>
<br>
<b>命题 6.2</b>：$\mathbb{Q}$ 可以按 $x\to\lbrack\{x\}\rbrack$ 嵌入 $\mathbb{R}$ ，并保持加法、乘法、相反数、倒数、序、绝对值.<br>
这个比较简单。 $\blacksquare$<br>
<br>
<b>命题 6.3</b>：$\mathbb{R}$ 关于其上的加法和乘法运算，以及零元 $\lbrack\{0\}\rbrack$ 和幺元 $\lbrack\{1\}\rbrack$ 构成一个域，具体来说：<br>
① $\mathbb{R}$ 上加法满足交换律和结合律；<br>
② 对任意 $x\in\mathbb{R}$ ，有 $x+\lbrack\{0\}\rbrack=x$ ；<br>
③ 对任意 $x\in\mathbb{R}$ ，存在唯一的 $y\in\mathbb{R}$ ，使得 $x+y=\lbrack\{0\}\rbrack$ ，且这里的 $y$ 是 $x$ 的相反数；<br>
④ $\mathbb{R}$ 上乘法满足交换律、结合律，以及关于加法的分配律；<br>
⑤ $\lbrack\{1\}\rbrack\neq\lbrack\{0\}\rbrack$ ，且对任意 $x\in\mathbb{R}$ ，有 $x\cdot\lbrack\{1\}\rbrack=x$ ；<br>
⑥ 对任意 $x\in\mathbb{R}\setminus\lbrack\{0\}\rbrack$ ，存在唯一的 $y\in\mathbb{R}$ ，使得 $x\cdot y=\lbrack\{1\}\rbrack$ ，且这里的 $y$ 是 $x$ 的倒数.<br>
这个照常省略。相信认真看到这里的人肯定会（ $\blacksquare$<br>
<br>
<i>当 $\mathbb{R}$ 作为域时，有和命题 5.3 的注记类似的基于域的性质.</i><br>
<br>
<b>命题 6.4</b>：$\mathbb{R}$ 关于 $\leq$ 构成线性序集，即对任意 $x,y\in\mathbb{R}$ ，有 $x\leq y$ 或 $y\leq x$ ，也即对任意 $x,y\in\mathbb{R}$ ，有 $x\lt y$ ，$x=y$ ，$x\gt y$ 三者恰成立其一.<br>
这个比较简单。 $\blacksquare$<br>
<br>
<b>命题 6.5</b>：$\mathbb{R}$ 上的加法和乘法运算关于序 $\leq$ 有一些熟知的性质，如<br>
① 对 $x,y,z\in\mathbb{R}$ ，有 $x\leq y$ 当且仅当 $x+z\leq y+z$ ，同时 $x\lt y$ 当且仅当 $x+z\lt y+z$ ；<br>
② 对 $x,y\in\mathbb{R}$ ，有 $x\cdot y\gt\lbrack\{0\}\rbrack$ 当且仅当 $x,y\gt\lbrack\{0\}\rbrack$ 或 $x,y\lt\lbrack\{0\}\rbrack$ ，同时 $x\cdot y\lt\lbrack\{0\}\rbrack$ 当且仅当 $x\lt\lbrack\{0\}\rbrack\lt y$ 或 $y\lt\lbrack\{0\}\rbrack\lt x$ ；<br>
③ 对 $x,y,z\in\mathbb{R}$ ，若 $z\gt\lbrack\{0\}\rbrack$ ，则 $x\leq y$ 当且仅当 $x\cdot z\leq y\cdot z$ ，且有 $x\lt y$ 当且仅当 $x\cdot z\lt y\cdot z$ ；若 $z\lt\lbrack\{0\}\rbrack$ ，则 $x\leq y$ 当且仅当 $x\cdot z\geq y\cdot z$ ，且有 $x\lt y$ 当且仅当 $x\cdot z\gt y\cdot z$ ；<br>
④ $\lbrack\{1\}\rbrack\gt\lbrack\{0\}\rbrack$ .<br>
这个也比较简单。 $\blacksquare$<br>
<br>
<b>命题 6.6</b>：设 $x\in\mathbb{R}$ ，若 $x\geq\lbrack\{0\}\rbrack$ ，则 $\operatorname{abs}(x)=x$ ；若 $x\lt\lbrack\{0\}\rbrack$ ，则 $\operatorname{abs}(x)=-x$ .<br>
这个也比较简单。 $\blacksquare$<br>
<br>
然后是几个较为好用的性质：<br>
<br>
<b>命题 6.7</b>：若 $x\in\mathbb{R}$ ，则存在 $n\in\mathbb{N}^+$ ，使得 $n\gt x$ .<br>
<b>证明</b>　若 $x\leq 0$ ，令 $n=1$ 即可；<br>
若 $x\gt 0$ ，设 $x$ 对应有理数基本列 $\{p_\cdot\}$ ，根据 $x$ 是基本列，可知存在自然数 $N$ ，使得 $m,n\gt N$ 时有 $\operatorname{abs}(p_m-p_n)\lt 1$ .<br>
这意味着当 $n\gt N$ 时有 $\operatorname{abs}(p_n-p_{N+1})\lt 1$ ，所以 $p_n\lt p_{N+1}+1$.<br>
从而 $\lbrack\{p_\cdot\}\rbrack\leq\lbrack\{p_{N+1}+1\}\rbrack$ ，故 $p_{N+1}+1\geq x$ ，这表明有理数 $q=p_{N+1}+2$ 满足 $q\gt x$ .<br>
设 $q$ 的既约表示是 $r/s$ ，而 $q\gt x\gt 0$ ，所以 $r\gt 0$ ，$s\gt 0$ .<br>
从而 $r$ 是正整数，且 $s\geq 1$ ，这表明正整数 $r\geq r/s=q\gt x$ . $\blacksquare$<br>
<br>
<b>命题 6.8</b>：$\lbrack\{1/n\}\rbrack=\lbrack\{0\}\rbrack$ .<br>
<b>证明</b>　对任意 $c\in\mathbb{Q}^+$ ，根据命题 6.7 ，存在自然数 $N$ ，使得 $N\gt 1/c$ .<br>
所以对自然数 $n\gt N$ ，都有 $n\gt 1/c$ ，故 $1/n\lt c$ ，故 $\operatorname{abs}(1/n-0)=1/n\lt c$ .<br>
这就证明了 $\lbrack\{1/n\}\rbrack=\lbrack\{0\}\rbrack$ . $\blacksquare$<br>
<br>
<b>命题 6.9</b>：若 $x,y\in\mathbb{R}$ ，$x\lt y$ ，则存在 $q\in\mathbb{Q}$ ，使得 $x\lt q\lt y$ .<br>
<b>证明</b>　由于 $y-x\gt 0$ ，故根据命题 6.7 ，存在正整数 $n$ ，使得 $n\gt 1/(y-x)$ .<br>
这表明 $1/n\lt y-x$ .<br>
根据命题 6.7 ，存在正整数 $m,m^*$ ，使得 $m\gt n\cdot x$ ，$m^*\gt -n\cdot x$ .<br>
设 $L = \{ k\in\mathbb{Z} \mid k/n\leq x \}$ ，则根据 $(-m^*)/n=-(m^*/n)\lt-((-n\cdot x)/n)=x$ ，可知 $-m^*\in L$ .<br>
且对任意 $k\in L$ ，一定有 $k\leq n\cdot x\lt m$ .<br>
故 $L$ 是 $\mathbb{Z}$ 的非空子集且有上界，故根据命题 4.16 ，$L$ 有最大元素，记为 $p$ .<br>
那么 $p\in L$ ，且 $p+1$ 不属于 $L$ ，故 $p/n\leq x$ ，$(p+1)/n\gt x$ ，所以 $x\lt(p+1)/n=p/n+1/n\leq x+1/n\lt x+(y-x)=y$ .<br>
这就得到有理数 $q=(p+1)/n$ 满足条件. $\blacksquare$<br>
<br>
<b>命题 6.10</b>：若 $x\in\mathbb{R}$ ，$\{q_\cdot\}$ 为有理数基本列，则：<br>
<b>证明</b>　① 若 $x\lt\lbrack\{q_\cdot\}\rbrack$ ，则存在自然数 $N$ ，使得对任意自然数 $n\gt N$ ，有 $x\lt q_n$ ；<br>
② 若 $x\gt\lbrack\{q_\cdot\}\rbrack$ ，则存在自然数 $N$ ，使得对任意自然数 $n\gt N$ ，有 $x\gt q_n$ .<br>
这里只证明①，因为②和①同理。<br>
<br>
设 $x\lt\lbrack\{q_\cdot\}\rbrack$ ，根据命题 6.9 ，取 $x'\in\mathbb{Q}$ ，使得 $x\lt x'\lt\lbrack\{q_\cdot\}\rbrack$<br>
再设 $x'=\lbrack\{p_\cdot\}\rbrack$ ，则对任意 $c\in\mathbb{Q}^+$ ：<br>
由 $\lbrack\{p_\cdot\}\rbrack=x'\lt\lbrack\{q_\cdot\}\rbrack$ 可知，存在自然数 $N_1$ ，使得对任意自然数 $n\gt N_1$ ，有 $p_n\leq q_n+c/3$ .<br>
而 $\{q_\cdot\}$ 是有理数基本列，所以存在自然数 $N_2$ ，使得对任意自然数 $m,n\gt N_2$ ，有 $-c/3\lt q_m-q_n\lt c/3$ .<br>
取 $N$ 为 $N_1$ 和 $N_2$ 的较大数，则当自然数 $n\gt N$ 时：<br>
对任意自然数 $m\gt N$ ，有 $p_m\leq q_m+c/3$ ， $-c/3\lt q_m-q_n\lt c/3$ .<br>
所以 $p_m\leq q_m+c/3\lt q_n+c/3+c/3$ .<br>
那么就有 $x'=\lbrack\{p_{\cdot+N+1}\}\rbrack\leq\lbrack\{q_n+c/3+c/3\}\rbrack=q_n+c/3+c/3\lt q_n+c$ .<br>
<br>
这表明对任意 $c\in\mathbb{Q}^+$ ，存在自然数 $N$ ，使得对任意自然数 $n\gt N$ 都有 $x'\lt q_n+c$ .<br>
特别地，根据命题 6.9 ，取有理数 $c$ 使得 $0\lt c\lt x'-x$ ，就可以得到对 $n\gt N$ 有 $q_n\gt x'-c\gt x$ . $\blacksquare$<br>
<br>
最后，我们来证明实数集 $\mathbb{R}$ 最重要的一条性质——柯西收敛准则：<br>
<br>
<b>命题 6.11</b>：若映射 $r : \mathbb{N}\to\mathbb{R}$ 满足：对任意 $c\in\mathbb{Q}^+$ ，都存在自然数 $N$ ，使得对任意自然数 $m,n\gt N$ 都有 $-c\lt r_m-r_n\lt c$ .<br>
<b>证明</b>　那么存在实数 $\eta$ ，使得对任意 $c\in\mathbb{Q}^+$ ，都存在自然数 $N$ ，使得对任意自然数 $n\gt N$ 都有 $\eta-c\lt r_n\lt\eta+c$ .<br>
我们定义有理数序列 $F : \mathbb{N}\to\mathbb{Q}$ ：根据命题 6.9 ，在 $r_n-1/n$ 和 $r_n+1/n$ 之间取有理数 $F_n$ . （这里 $F_n$ 是某个集合的最大值，所以可以对应递归函数，应该不涉及逻辑问题）<br>
<br>
然后，对任意 $c\in\mathbb{Q}^+$ ，存在自然数 $N_1$ ，使得对任意自然数 $m,n\gt N_1$ 有 $-c/2\lt r_m-r_n\lt c/2$ .<br>
也存在自然数 $N_2$ ，使得 $N_2\gt 1/(4\cdot c)$ .<br>
取 $N$ 为 $N_1$ 和 $N_2$ 的较大数，则对任意自然数 $m,n\gt N$ ，有 $-c/2\lt r_m-r_n\lt c/2$ ，$1/m+1/n\lt c/2$ .<br>
所以结合 $r_m-1/m\lt F_m\lt r_m+1/m$ ，$r_n-1/n\lt F_n\lt r_n+1/n$ ，故 $-c\lt F_m-F_n\lt c$ .<br>
故 $\{F_\cdot\}$ 是有理数基本列，取 $\eta=\lbrack\{F_\cdot\}\rbrack$ .<br>
<br>
根据命题 6.8 ，又有 $\eta=\lbrack\{F_n-1/n\}\rbrack=\lbrack\{F_n+1/n\}\rbrack$ .<br>
<br>
由于 $F_n-1/n\lt r_n\lt F_n+1/n$ ，故 $F_n-1/n-\eta\lt r_n-\eta\lt F_n+1/n-\eta$ .<br>
<br>
而对任意 $c\in\mathbb{Q}^+$ ，由于 $\eta-c\lt\eta=\lbrack\{F_n-1/n\}\rbrack$ ，故根据命题 6.10 ，存在自然数 $N_3$ ，使得对任意自然数 $n\gt N_3$ 有 $\eta-c\lt F_n-1/n$ .<br>
由于 $\eta+c\gt\eta=\lbrack\{F_n+1/n\}\rbrack$ ，故根据命题 6.10 ，存在自然数 $N_4$ ，使得对任意自然数 $n\gt N_4$ 有 $\eta+c\gt F_n+1/n$ .<br>
所以当 $n\gt N_3$ 且 $n\gt N_4$ 时，有 $-c\lt F_n-1/n-\eta$ ，$F_n+1/n-\eta\lt c$ .<br>
<br>
取 $N$ 为 $N_3$ 和 $N_4$ 的较大数，则对任意自然数 $n\gt N$ ，有 $-c\lt F_n-1/n-\eta$ ，$F_n+1/n-\eta\lt c$ ，即 $-c\lt r_n-\eta\lt c$ .<br>
<br>
这就证明了结论。 $\blacksquare$<br>
<br><br>
至此，我们构建了实数集 $\mathbb{R}$ ，并证明了实数系基本定理之一：柯西收敛准则。<br>
<br>
那么，《微积分》或《数学分析》的内容就可以真正开始了。<br>
<br>
本质上，《微积分》或《数学分析》教材的起步都是如下的约定：<br>
①实数集 $\mathbb{R}$ 关于 $0$ ，$1$ ，加法，乘法是一个域；<br>
②实数集 $\mathbb{R}$ 上有一个线性序 $\leq$ ，满足不等号两边可以同时加一个元素，且两个非负实数的乘积还是非负实数；<br>
③实数集 $\mathbb{R}$ 有完备性，即实数系基本定理都成立。<br>
<br>
而我们已经完成了这些内容，所以《微积分》或《数学分析》课程的内容至此真的可以开始了！！！<br>
<br>
那么本文的主要内容就到此为止了。<br>
<br>
接下来可以再做一个补充内容：正实数的进制表示。这部分内容将基于之前证明的一些实数集的性质，以及一些微积分知识。<br>

<br><br>


## 第七章  正实数的进制表示（补充内容）<br>
<br>
基于前面的内容，我们可以发展出《微积分》或《数学分析》课程的体系。<br>
<br>
因此，接下来的内容我们将默认基础的数列极限知识。同时，四则运算中的乘法符号「$\cdot$」将被省略，或写作「$*$」.<br>
<br>
<b>首先，我们需要定义底数为正实数，幂为整数的乘方：</b><br>
<br>
对正实数 $A$ ，我们用如下方式定义乘方 $A^n$ ：<br>
① $A^0=1$ ；<br>
② $A^{n+1}=A\cdot(A^n)$ .<br>
<br>
通过 ② 也可以得到 $A^{n-1}=(1/A)\cdot(A^n)$ .<br>
如此归纳定义即可唯一确定一切整数 $n$ 下的 $A^n$ 的值。<br>
<br>
<b>命题 7.1</b>：对正实数 $A$ 以及整数 $m,n$ ，有 $A^{m+n}=(A^m)\cdot(A^n)$ .<br>
<b>证明</b>　直接使用数学归纳法，对 $n$ 归纳即可。 $\blacksquare$<br>
<br>
<b>命题 7.2</b>：对正实数 $A$ 以及整数 $n$ ，有 $A^n\gt 0$ .<br>
<b>证明</b>　对 $n$ 归纳即可，不过需要两个方向的归纳。 $\blacksquare$<br>
<br>
<i>命题 7.1 和 7.2 是非常符合直觉的常识，因此后面可能不加引用直接默认。</i><br>
<br>
<b>命题 7.3</b>：对任意正实数 $b\geq 2$ 及非负整数 $n$ ，均有 $b^n\gt n$ .<br>
<b>证明</b>　对 $n$ 归纳：<br>
一方面，对 $n=0$ 有 $b^0=1\gt 0=n$ ；<br>
另一方面，假设 $b^n\gt n$ ，则根据命题 3.7 有 $b^n\geq n+1$ ，所以 $b^{n+1}=b\cdot(b^n)\geq b\cdot(n+1)\geq 2\cdot(n+1)=n+n+2\geq n+2\gt n+1$ .<br>
所以根据数学归纳法，有 $b^n\gt n$ 成立。 $\blacksquare$<br>
<br>
<b>命题 7.4</b>：对任意正实数 $b\gt 1$ 及整数 $n$ ，均有 $b^n\lt b^{n+1}$ .<br>
<b>证明</b>　$b^{n+1}=b\cdot(b^n)\geq 2\cdot(b^n)\gt b^n$ . $\blacksquare$<br>
<br>
<b>命题 7.5</b>：对任意正实数 $b\geq 2$ 及正实数 $c$ ，存在整数 $m,n$ ，使得 $b^m\gt c$ ，$b^n\lt c$ .<br>
<b>证明</b>　根据命题 6.7 ，存在正整数 $m,k$ ，使得 $m\gt c$ ，$k\gt 1/c$ .<br>
取 $n=-k$ ，再结合命题 7.3 ，就有 $b^m\gt m\gt c$ ，$b^{-n}=b^k\gt k\gt 1/c$ ，从而 $b^n\lt c$ . $\blacksquare$<br>
<br>
<b>命题 7.6</b>：对正实数 $b\geq 2$ 以及正实数 $r$ ，存在唯一的整数 $n$ ，使得 $b^n\leq r\lt b^{n+1}$ .<br>
<b>证明</b>　设 $L = \{ k\in\mathbb{Z} \mid b^k\leq r \}$ ，根据命题 7.4 和 7.5 可知：<br>
① 集合 $L$ 非空，集合 $\mathbb{Z}\setminus L$ 非空；<br>
② 对任意 $x\in L$ 以及整数 $y\lt x$ ，有 $y\in L$ ；<br>
③ 对任意 $x\in\mathbb{Z}\setminus L$ 以及整数 $y\gt x$ ，有 $y\in\mathbb{Z}\setminus L$ .<br>
于是，根据命题 4.16 ，可以得到 $L$ 有最大元素 $n$ .<br>
根据 $n$ 的最大性，有 $b^n\leq r$ ，$b^{n+1}\gt r$ ，所以 $n$ 满足条件；<br>
再根据性质 ② ，满足条件的 $n$ 一定是集合 $L$ 的最大元素，所以这样的 $n$ 是唯一的。 $\blacksquare$<br>
<br>
<i>不难得到，对整数 $k$ ，有 $b^k\leq r$ 当且仅当 $k\leq n$ ，这个结论也将直接引用。</i><br>
<br>
<b>那么，接下来就可以定义正实数的进制表示了。</b><br>
<br>
首先，给定了正整数 $b\geq 2$ 后，每个 $b$ 进制表示是一个从 $\mathbb{Z}$ 到 $\{ k\in\mathbb{N} \mid k\lt b \} = \{0,1,2,\dots,b-1\}$ 的映射。<br>
<br>
从而对正实数 $r$ ，我们用 $F_{b,r}(n)$ 表示 $r$ 的 $b$ 进制表示在整数 $n$ 下的像。<br>
<br>
设 $r$ 是正实数，正整数 $b\geq 2$ ，用如下方式归纳地定义进制表示 $F_{b,r}(n)$ ：<br>
<br>
首先，根据命题 7.6 ，存在唯一的整数 $N$，使得 $b^N\leq r\lt b^{N+1}$ .<br>
此时，<b>规定当 $n\gt N$ 时，均有 $F_{b,r}(n)=0$ .</b><br>
与此同时，根据命题 4.16 和 6.7（这个事实较为显然，以后不再引用命题），存在唯一的整数 $k(N)$ ，使得 $k(N)\leq r/(b^N)\lt k(N)+1$ .<br>
由于 $1\leq r/(b^N)\lt b$ ，故 $1\leq k(N)\leq b-1$ ，<b>此时规定 $F_{b,r}(N)=k(N)$ .</b><br>
<br>
然后根据 $F_{b,r}(N)$ 的性质，有 $0 \leq r - F_{b,r}(N)\cdot b^N \lt b^N$ ，所以存在唯一的整数 $k(N-1)$ ，使得<br>
$k(N-1)\leq ( r - F_{b,r}(N)\cdot b^N ) / b^{N-1} \lt k(N-1)+1$ ，且 $0 \leq k(N-1) \leq b-1$ .<br>
<b>此时规定 $F_{b,r}(N-1)=k(N-1)$ .</b><br>
根据 $F_{b,r}(N-1)$ 的性质又有 $0 \leq r - F_{b,r}(N)\cdot b^N - F_{b,r}(N-1)\cdot b^{N-1} \lt b^{N-1}$ .<br>
<br>
以此类推，当 $F_{b,r}(N)$ , $F_{b,r}(N-1)$ , $F_{b,r}(N-2)$ , ... , $F_{b,r}(N-m)$ 均已经定义，且保证<br>
$0 \leq r - F_{b,r}(N)\cdot b^N - F_{b,r}(N-1)\cdot b^{N-1} - \dots - F_{b,r}(N-m)\cdot b^{N-m} \lt b^{N-m}$ .<br>
<br>
那么存在唯一的整数 $k(N-m-1)$ ，使得<br>
$k(N-m-1) \leq ( r - F_{b,r}(N)\cdot b^N - F_{b,r}(N-1)\cdot b^{N-1} - \dots - F_{b,r}(N-m)\cdot b^{N-m} ) / b^{N-m-1} \lt k(N-m-1)+1$ .<br>
且 $0 \leq k(N-m-1) \leq b-1$ .<br>
<b>此时规定 $F_{b,r}(N-m-1)=k(N-m-1)$ .</b><br>
<br>
根据 $F_{b,r}(N-m-1)$ 的性质，又有  $0 \leq r - F_{b,r}(N)\cdot b^N - F_{b,r}(N-1)\cdot b^{N-1} - \dots - F_{b,r}(N-m)\cdot b^{N-m} - F_{b,r}(N-m-1)\cdot b^{N-m-1} \lt b^{N-m-1}$ .<br>
<br>
如此归纳，就对每个整数 $n$ 都定义了 $F_{b,r}(n)$ 的值，于是这就得到了正实数 $r$ 的 $b$ 进制表示。<br>
<br>
定义完毕后，我们自然需要提出一些非常容易想到的问题：<br>
1.　不同的实数是否会具备同样的进制表示？<br>
2.　进制表示有什么含义？<br>
3.　哪些 $\mathbb{Z}$ 到 $\{0,1,\dots,b-1\}$ 的映射才是某个正实数的进制表示？<br>
<br>
我们将用三个命题分别回答这三个问题。<br>
<br>
<b>命题 7.7</b>：给定正整数 $b\geq 2$ ，若正实数 $r,s$ 满足对任意整数 $n$ 都有 $F_{b,r}(n)=F_{b,s}(n)$ ，则 $r=s$ .<br>
<b>证明</b>　根据进制表示的定义方式，存在整数 $N$ 同时满足 $b^N \leq r \lt b^{N+1}$ ，$b^N \leq s \lt b^{N+1}$ .<br>
再根据进制表示的归纳定义过程，对任意正整数 $m$ ，均有<br>
$0 \leq r - F_{b,r}(N)\cdot b^N - F_{b,r}(N-1)\cdot b^{N-1} - \dots - F_{b,r}(N-m)\cdot b^{N-m} \lt b^{N-m}$ .<br>
$0 \leq s - F_{b,s}(N)\cdot b^N - F_{b,s}(N-1)\cdot b^{N-1} - \dots - F_{b,s}(N-m)\cdot b^{N-m} \lt b^{N-m}$ .<br>
<br>
既然 $F_{b,r}(n)=F_{b,s}(n)$ 对任意整数 $n$ 恒成立，故 $r,s$ 都不小于 $F_{b,r}(N)\cdot b^N - F_{b,r}(N-1)\cdot b^{N-1} - \dots - F_{b,r}(N-m)\cdot b^{N-m}$ ，<br>
且都小于 $F_{b,r}(N)\cdot b^N - F_{b,r}(N-1)\cdot b^{N-1} - \dots - F_{b,r}(N-m)\cdot b^{N-m} + b^{N-m}$ .<br>
所以 $|r-s|\lt b^{N-m}$ .<br>
假设 $r\neq s$ ，那么对任意正整数 $m$ 都有 $b^m\lt(b^N)/|r-s|$ ，这和命题 7.6 的补充内容矛盾。<br>
所以必有 $r=s$ . $\blacksquare$<br>
<br>
<b>命题 7.8</b>：给定正整数 $b\geq 2$ ，对正实数 $r$ ，根据命题 7.6，存在唯一的整数 $N$ 满足 $b^N\leq r\lt b^{N+1}$，若进一步定义数列 $p(n)=F_{b,r}(N)\cdot b^N+F_{b,r}(N-1)\cdot b^{N-1}+\dots+F_{b,r}(N-n)\cdot b^{N-n}$ ，则数列 $p(n)$ 的极限为 $r$ .<br>
<b>证明</b>　根据进制表示的归纳定义部分，有<br>
$0 \leq r - F_{b,r}(N)\cdot b^N - F_{b,r}(N-1)\cdot b^{N-1} - \dots - F_{b,r}(N-n)\cdot b^{N-n} \lt b^{N-n}$ .<br>
这意味着 $0 \leq r - p(n) \lt b^{N-n}$ ，从而 $p(n) \leq r$ .<br>
由于 $p(n)$ 显然单调递增，故 $p(n)$ 存在极限.<br>
再对不等式 $0 \leq r - p(n) \lt b^{N-n}$ 的每一部分同时取极限，就得到 $p(n)$ 的极限为 $r$ . $\blacksquare$<br>
<br>
<b>命题 7.9</b>：给定正整数 $b\geq 2$ ，对映射 $T : \mathbb{Z} \to \{ 0 , 1 , 2 , \dots , b-1 \}$ ，「存在正实数 $r$ 使得 $F_{b,r}(n)=T(n)$ 」 的充分必要条件是下面两个条件都成立：<br>
<b>证明</b>　① 存在整数 $N$ ，使得 $T(N)\neq 0$ ，且对任意整数 $n\gt N$ 均有 $T(n)=0$ ；<br>
② 对任意整数 $K$ ，都存在整数 $n\lt K$ ，使得 $T(n)\neq b-1$ .<br>
（1）首先证明必要性：若存在正实数 $r$ 使得 $F_{b,r}(n)=T(n)$ ，根据进制表示的定义方式即可知道条件 ① 满足，设整数 $N$ 满足 $b^N\leq r\lt b^{N+1}$ .<br>
然后验证条件 ② ：假设存在整数 $K$ ，使得 $n\lt K$ 时均有 $T(n)=b-1$ .<br>
<br>
由于 $F_{b,r}(N+1)=0\neq b-1$ ，故这样的 $K$ 必定不超过 $N+1$ ，那么不妨设 $K$ 就是最大的可能值，即 $T(K)\neq b-1$ ，且 $b-1=T(K-1)=T(K-2)=\dots$ .<br>
<br>
设整数 $N$ 满足 $b^N\leq r\lt b^{N+1}$ ，定义数列 $p(n) = T(N)\cdot b^N + T(N-1)\cdot b^{N-1} + \dots + T(N-n)\cdot b^{N-n}$ .<br>
那么根据命题 7.8 ，可知 $p(n)$ 的极限为 $r$ .<br>
<br>
假设 $K=N+1$ ，那么 $p(n) = T(N)\cdot b^N + T(N-1)\cdot b^{N-1} + \dots + T(N-n)\cdot b^{N-n} = (b-1)\cdot(b^N+b^{N-1}+\dots+b^{N-n})$ .<br>
根据极限知识，可知 $p(n)$ 的极限为 $b^{N+1}$ ，所以 $r=b^{N+1}$ ，这和 $b^N\leq r\lt b^{N+1}$ 矛盾。<br>
从而 $K\leq N$ .<br>
<br>
设 $k=N-K$ ，则 $k$ 是自然数，且 $T(N-k)\lt b-1$ ，$b-1=T(N-k-1)=T(N-k-2)=\dots$ .<br>
此时对正整数 $n\gt k$ 均有<br>
$p(n) = T(N)\cdot b^N + T(N-1)\cdot b^{N-1} + \dots + T(N-n)\cdot b^{N-n}$<br>
$= T(N)\cdot b^N + T(N-1)\cdot b^{N-1} + \dots + T(N-k)\cdot b^{N-k} + T(N-k-1)\cdot b^{N-k-1} + \dots + T(N-n)\cdot b^{N-n}$<br>
$= T(N)\cdot b^N + T(N-1)\cdot b^{N-1} + \dots + T(N-k)\cdot b^{N-k} + (b-1)\cdot b^{N-k-1} + \dots + (b-1)\cdot b^{N-n}$<br>
<br>
根据极限知识，可知 $(b-1)\cdot b^{N-k-1} + \dots + (b-1)\cdot b^{N-n}$ 的极限是 $b^{N-k}$，所以又得到 $p(n)$ 的极限是<br>
$T(N)\cdot b^N + T(N-1)\cdot b^{N-1} + \dots + (T(N-k)+1)\cdot b^{N-k}$<br>
<br>
所以 $r = T(N)\cdot b^N + T(N-1)\cdot b^{N-1} + \dots + (T(N-k)+1)\cdot b^{N-k}$ .<br>
但根据进制表示的归纳定义过程，又有 $0 \leq r - T(N)\cdot b^N - T(N-1)\cdot b^{N-1} - \dots - T(N-k)\cdot b^{N-k} \lt b^{N-k}$ .<br>
这就得到 $0 \leq b^{N-k} \lt b^{N-k}$ ，矛盾。<br>
<br>
这就证明了必要性。<br>
<br>
（2）然后考虑充分性：若 $T(n)$ 满足两个条件，设 $N$ 是条件 ① 中的 $N$ ，根据命题 7.6 可知这样的 $N$ 唯一。<br>
然后定义数列 $p(n) = T(N)\cdot b^N + T(N-1)\cdot b^{N-1} + \dots + T(N-n)\cdot b^{N-n}$ .<br>
<br>
由于 $p(n)\geq T(N)\cdot b^N\geq T(N)$ ，且条件 ② 确保我们可以取正整数 $k$ ，使得 $T(N-k)\lt b-1$ ，即可得到当 $n\gt k$ 时有<br>
$$\begin{aligned}
p(n) &= T(N)\cdot b^N + T(N-1)\cdot b^{N-1} + \dots + T(N-n)\cdot b^{N-n} \\
&\leq T(N)\cdot b^N + (b-1)\cdot b^{N-1} + \dots + (b-1)\cdot b^{N-n} - b^{N-k} \lt T(N)\cdot b^N + b^N - b^{N-k}.
\end{aligned}$$<br>
故 $p(n)$ 一定存在极限 $r$ ，且 $T(N) \leq r \leq T(N)\cdot b^N + b^N - b^{N-k}$ ，故 $T(N) \leq r \lt (T(N)+1)\cdot b^N$ .<br>
<br>
一方面，根据 $0 \lt T(N) \leq b-1$ ，可以得到 $b^N \leq r \lt b^{N+1}$ .<br>
另一方面，对非负整数 $n$ ，条件 ② 确保我们可以取正整数 $k$ ，使得 $T(N-n-k)\lt b-1$ .<br>
故对正整数 $m\gt n+k$ ，有<br>
$$\begin{aligned}
&p(m) - T(N)\cdot b^N - T(N-1)\cdot b^{N-1} - \dots - T(N-n)\cdot b^{N-n} \\
&= T(N-n-1)\cdot b^{N-n-1} + T(N-n-2)\cdot b^{N-n-2} + \dots + T(N-n-m)\cdot b^{N-n-m}
\end{aligned}$$<br>
从而$$\begin{aligned}
0 &\leq p(m) - T(N)\cdot b^N - T(N-1)\cdot b^{N-1} - \dots - T(N-n)\cdot b^{N-n} \\
&\leq (b-1)\cdot(b^{N-n-1} + b^{N-n-2} + \dots + b^{N-n-m}) - b^{N-n-k} \lt b^{N-n} - b^{N-n-k}
\end{aligned}$$<br>
两边让 $m$ 趋近于无穷，同时取极限，就能得到 $0 \leq r - T(N)\cdot b^N - T(N-1)\cdot b^{N-1} - \dots - T(N-n)\cdot b^{N-n} \leq b^{N-n} - b^{N-n-k} \lt b^{N-n}$ .<br>
<br>
于是这就得到下面的结论。<br>
结论一：$b^N \leq r \lt b^{N+1}$ ；<br>
结论二：$T(N)\gt 0$ ，$0=T(N+1)=T(N+2)=\dots$ ；<br>
结论三：对非负整数 $n$ 均有 $0 \leq r - T(N)\cdot b^N - T(N-1)\cdot b^{N-1} - \dots - T(N-n)\cdot b^{N-n} \lt b^{N-n}$ .<br>
<br>
根据结论一又可以得到<br>
结论四：$F_{b,r}(N)\gt 0$ ，$0=F_{b,r}(N+1)=F_{b,r}(N+2)=\dots$ ；<br>
<br>
最后，根据进制表示归纳定义的部分，可知<br>
结论五：对非负整数 $n$ 均有 $0 \leq r - F_{b,r}(N)\cdot b^N - F_{b,r}(N-1)\cdot b^{N-1} - \dots - F_{b,r}(N-n)\cdot b^{N-n} \lt b^{N-n}$ .<br>
<br>
最后归纳证明对任意自然数 $n$ 都有 $T(N-n)=F_{b,r}(N-n)$ .<br>
对 $n=0$ ，我们将结论三和结论五结合，即可得到 $|T(N)\cdot b^N-F_{b,r}(N)\cdot b^N|\lt b^N$ ，所以 $|T(N)-F_{b,r}(N)|\lt 1$ ，从而 $T(N)=F_{b,r}(N)$ .<br>
假设结论已经对 $0,1,2,\dots,n-1$ 成立，将结论三和结论五结合，即可得到 $|T(N-n)\cdot b^{N-n}-F_{b,r}(N-n)\cdot b^{N-n}|\lt b^{N-n}$.<br>
所以 $|T(N-n)-F_{b,r}(N-n)|\lt 1$ ，从而 $T(N-n)=F_{b,r}(N-n)$ .<br>
<br>
所以根据数学归纳法，有<br>
结论六：对任意自然数 $n$ 都有 $T(N-n)=F_{b,r}(N-n)$ .<br>
<br>
综合结论二、四、六，即可得到 $r$ 满足条件，充分性成立。 $\blacksquare$<br>
<br><br>
那么正实数的进制表示到此就结束了。<br>
<br>
零作为平凡的常数无需额外考虑，而若要表示负数，只需要用进制表示它的绝对值，再加上负号标明即可。<br>
<br>
这样就得到了完整的进制表示和体系。<br>
<br>
本文完。<br>








