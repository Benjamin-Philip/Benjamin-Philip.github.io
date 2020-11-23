(define (func i)
  (cond (<= i 0)
  (begin
        (display i)
        (func (- i 1)))))
