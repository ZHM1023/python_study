
from rdwt import rdwt

list01 = [["name", "age", "sex", "score"],
          ["Tom", 21, "Man", 101],
          ["Jerry", 21, "Woman", 60.5],
          ["Hale", 23, "Man", 79],
          ["Role", 30, "Woman", 100]]

rdwt.writable(list01, "./testmoudle.xlsx")

