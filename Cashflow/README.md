## Cashflow diagram:

`import cashflow`

`cashflow.diagram (time, value, cashflow, 'g', 'k', '$', 'diagram.png', [12,9], bar = False)`

Parameter | Explanation | example
----------- | ------------------- |--------------------------
|`t`				| time array					|`[2000, 2001, 2002]`|
|`value` 		| value array					| `[20, 24, 23]`|
|`cashflow` | cashflow array 			| `[2, 2, 2]`|
|`c1`				| value color 			 	| `'r', 'g', 'b', '#FF0099'`|
|`c2`				| cashflow color 		 	| `'r', 'g', 'b', '#FF0099'`|
|`currency`	| currency label			| `'$', 'NT$', 'HK$'`|
|`path`			| output file					| `'../folder/image.png'`|	
|`baspect` 	| aspect ratio array	| `[12, 9], [4, 3]` |
|`int_x`		| integer x axis			| `'True', 'False'`|
|`show`			| show plot 					| `'True', 'False'`|
|`bar`			| bar graph or plot 	| `'True', 'False'`|

