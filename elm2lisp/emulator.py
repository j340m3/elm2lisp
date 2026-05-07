import hy

code = """
; hidden helper
(defn __dec [a] (- a 1))
(defn __inc [a] (+ a 1))

; ulisp builtins
(defn 1- [#* values]
    (list (map __dec values)))
(defn 1+ [#* values]
    (list (map __inc values)))
(setv 1-.__doc__ "Decrements the value by one")
(defn ? [a]
    (. a __doc__))

(print '(a b))
; (print (. 1- __doc__))
"""


print(hy.eval(hy.read_many(code)))
