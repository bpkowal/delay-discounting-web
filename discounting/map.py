class Room(object):

    def __init__(self, ss_a, ss_d, ll_a, ll_d):
        self.ss_a = ss_a
        self.ss_d = ss_d
        self.ll_a = ll_a
        self.ll_d = ll_d
    	self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

#class Ind_Point(object):

#    def __init__(self, Ind_Point):
#        self.Ind_Point = Ind_Point
        


# Trial 1 $5.00
central_corridor = Room("$5.00", "TODAY", "$10", "IN 1 DAY")

central_corridor_2 = Room("$5.00", "TODAY", "$10", "IN 7 DAYS")

central_corridor_3 = Room("$5.00", "TODAY", "$10", "IN 30 DAYS")

central_corridor_4 = Room("$5.00", "TODAY", "$10", "IN 180 DAYS")

central_corridor_5 = Room("$5.00", "TODAY", "$10", "IN 365 DAYS")

central_corridor_6 = Room("$5.00", "TODAY", "$10", "IN 1825 DAYS")

central_corridor_7 = Room("$5.00", "TODAY", "$10", "IN 9125 DAYS")

# Trial 2 $2.50
up_one = Room("$7.50", "TODAY", "$10", "IN 1 DAY")

#Trial 3 $1.25
up_one_d1 = Room("$6.25", "TODAY", "$10", "IN 1 DAY")

up_two = Room("$8.75", "TODAY", "$10", "IN 1 DAY")

#Trial 4 $0.625
up_one_d1_u1 = Room("$6.88", "TODAY", "$10", "IN 1 DAY")

up_one_d2 = Room("$5.63", "TODAY", "$10", "IN 1 DAY")

up_three = Room("$9.38", "TODAY", "$10", "IN 1 DAY")

up_two_d1 = Room("$8.13", "TODAY", "$10", "IN 1 DAY")

#Trial 5 $0.3125
up_one_d1_u1_d1 = Room("$6.57", "TODAY", "$10", "IN 1 DAY")
up_one_d1_u2 = Room("$7.51", "TODAY", "$10", "IN 1 DAY")

up_one_d2_u1 = Room("$5.94", "TODAY", "$10", "IN 1 DAY")
up_one_d3 = Room("$5.32", "TODAY", "$10", "IN 1 DAY")

up_two_d2 = Room("$7.82", "TODAY", "$10", "IN 1 DAY")
up_two_d1_u1 = Room("$8.44", "TODAY", "$10", "IN 1 DAY")

up_three_d1 = Room("$9.07", "TODAY", "$10", "IN 1 DAY")
up_four = Room("$9.69", "TODAY", "$10", "IN 1 DAY")

#Finish $0.156
up_one_d1_u1_d1_u1 = Room("$6.73", "Task Complete", "IN 1 DAY", "Thank you")
up_one_d1_u1_d2 = Room("$6.41","Task Complete", "IN 1 DAY", "Thank you")
up_one_d1_u3 = Room("$7.67", "Task Complete", "IN 1 DAY", "Thank you")
up_one_d1_u2_d1 = Room("$7.35", "Task Complete", "IN 1 DAY", "Thank you")

up_one_d2_u2 = Room("$6.10", "Task Complete", "IN 1 DAY", "Thank you")
up_one_d2_u1_d1 = Room("$5.78", "Task Complete", "IN 1 DAY", "Thank you")
up_one_d3_u1 = Room("$5.48", "Task Complete", "IN 1 DAY", "Thank you")
up_one_d4 = Room("$5.16", "Task Complete", "IN 1 DAY", "Thank you")

up_two_d2_u1 = Room("$7.98", "Task Complete", "IN 1 DAY", "Thank you")
up_two_d3 = Room("$7.66", "Task Complete", "IN 1 DAY", "Thank you")
up_two_d1_u2 = Room("$8.60", "Task Complete", "IN 1 DAY", "Thank you")
up_two_d1_u1_d1 = Room("$8.28", "Task Complete", "IN 1 DAY", "Thank you")

up_three_d1_u1 = Room("$9.23", "Task Complete", "IN 1 DAY", "Thank you")
up_three_d2 = Room("$8.91", "Task Complete", "IN 1 DAY", "Thank you")
up_four_d1 = Room("$9.53", "Task Complete", "IN 1 DAY", "Thank you")
up_five = Room("$9.85", "Task Complete", "IN 1 DAY", "Thank you")

#Trial 2 $2.50
down_one = Room("$2.50", "TODAY", "$10", "IN 1 DAY")

#Trial 3  $1.25
down_one_u1 = Room("$3.75", "TODAY", "$10", "IN 1 DAY")
down_two = Room("$1.25", "TODAY", "$10", "IN 1 DAY")

#Trial 4  $0.6250
down_one_u2 = Room("$4.38", "TODAY", "$10", "IN 1 DAY")

down_one_u1_d1 = Room("$3.13", "TODAY", "$10", "IN 1 DAY")

down_two_u1 = Room("$1.88", "TODAY", "$10", "IN 1 DAY")

down_three = Room("$0.63", "TODAY", "$10", "IN 1 DAY")

#Trial 5 $0.3125
down_one_u3 = Room("$4.69", "TODAY", "$10", "IN 1 DAY")
down_one_u2_d1 = Room("$4.07", "TODAY", "$10", "IN 1 DAY")

down_one_u1_d2 = Room("$2.82", "TODAY", "$10", "IN 1 DAY")
down_one_u1_d1_u1 = Room("$3.44", "TODAY", "$10", "IN 1 DAY")

down_two_u1_d1 = Room("$1.57", "TODAY", "$10", "IN 1 DAY")
down_two_u2 = Room("$2.19", "TODAY", "$10", "IN 1 DAY")

down_three_u1 = Room("0.94", "TODAY", "$10", "IN 1 DAY")
down_four = Room("$0.31", "TODAY", "$10", "IN 1 DAY")

#Final $0.156
down_one_u4 = Room("$4.85","Task Complete", "IN 1 DAY", "Thank you")
down_one_u3_d1 = Room("$4.53", "Task Complete", "IN 1 DAY", "Thank you")
down_one_u2_d1_u1 = Room("$4.23", "Task Complete", "IN 1 DAY", "Thank you")
down_one_u2_d2 = Room("$3.91", "Task Complete", "IN 1 DAY", "Thank you")

down_one_u1_d2_u1 = Room("$2.98", "Task Complete", "IN 1 DAY", "Thank you")
down_one_u1_d3 = Room("$2.66", "Task Complete", "IN 1 DAY", "Thank you")
down_one_u1_d1_u2 = Room("$3.60","Task Complete", "IN 1 DAY", "Thank you")
down_one_u1_d1_u1_d1 = Room("$3.28", "Task Complete", "IN 1 DAY", "Thank you")

down_two_u1_d1_u1 = Room("$1.73", "Task Complete", "IN 1 DAY", "Thank you")
down_two_u1_d2 = Room("$1.41", "Task Complete", "IN 1 DAY", "Thank you")
down_two_u3 = Room("$2.35", "Task Complete", "IN 1 DAY", "Thank you")
down_two_u2_d1 = Room("$2.03", "Task Complete", "IN 1 DAY", "Thank you")

down_three_u2 = Room("$1.10", "Task Complete", "IN 1 DAY", "Thank you")
down_three_u1_d1 = Room("$0.78", "Task Complete", "IN 1 DAY", "Thank you")
down_four_u1 = Room("$0.47", "Task Complete", "IN 1 DAY", "Thank you")
down_five = Room("$0.15", "Task Complete", "IN 1 DAY", "Thank you")


#trial 1
central_corridor.add_paths({
    'v' : down_one,
    'n' : up_one
})

#trial 2
up_one.add_paths({
    'v' : up_one_d1,
    'n' : up_two
})

#trial 3
up_one_d1.add_paths({
    'v' : up_one_d2,
    'n' : up_one_d1_u1
})
up_two.add_paths({
    'v' : up_two_d1,
    'n' : up_three
})

#trial 4
up_one_d2.add_paths({
    'v' : up_one_d3,
    'n' : up_one_d2_u1
})
up_one_d1_u1.add_paths({
    'v' : up_one_d1_u1_d1,
    'n' : up_one_d1_u2
})
up_two_d1.add_paths({
    'v' : up_two_d2,
    'n' : up_two_d1_u1
})
up_three.add_paths({
    'v' : up_three_d1,
    'n' : up_four
})

#trial 5
up_one_d1_u1_d1.add_paths({
    'v' : up_one_d1_u1_d2,
    'n' : up_one_d1_u1_d1_u1
}) 
up_one_d1_u2.add_paths({
    'v' : up_one_d1_u2_d1,
    'n' : up_one_d1_u3
}) 
up_one_d2_u1.add_paths({
    'v' : up_one_d2_u1_d1,
    'n' : up_one_d2_u2
}) 
up_one_d3.add_paths({
    'v' : up_one_d4,
    'n' : up_one_d3_u1
}) 
up_two_d2.add_paths({
    'v' : up_two_d3,
    'n' : up_two_d2_u1
}) 
up_two_d1_u1.add_paths({
    'v' : up_two_d1_u1_d1,
    'n' : up_two_d1_u2
}) 
up_three_d1.add_paths({
    'v' : up_three_d2,
    'n' : up_three_d1_u1
})
up_four.add_paths({
    'v' : up_four_d1,
    'n' : up_five
}) 


#trial 2
down_one.add_paths({
    'v' : down_two,
    'n' : down_one_u1
})

#trial 3
down_one_u1.add_paths({
    'v' : down_one_u1_d1,
    'n' : down_one_u2
})
down_two.add_paths({
    'v' : down_three,
    'n' : down_two_u1
})

#trial 4
down_one_u2.add_paths({
    'v' : down_one_u2_d1,
    'n' : down_one_u3
})
down_one_u1_d1.add_paths({
    'v' : down_one_u1_d2,
    'n' : down_one_u1_d1_u1
}) 
down_two_u1.add_paths({
    'v' : down_two_u1_d1,
    'n' : down_two_u2
})
down_three.add_paths({
    'v' : down_four,
    'n' : down_three_u1
})

#trial 5
down_one_u3.add_paths({
    'v' : down_one_u3_d1,
    'n' : down_one_u4
}) 
down_one_u2_d1.add_paths({
    'v' : down_one_u2_d2,
    'n' : down_one_u2_d1_u1
}) 
down_one_u1_d2.add_paths({
    'v' : down_one_u1_d3,
    'n' : down_one_u1_d2_u1
}) 
down_one_u1_d1_u1.add_paths({
    'v' : down_one_u1_d1_u1_d1,
    'n' : down_one_u1_d1_u2
}) 
down_two_u1_d1.add_paths({
    'v' : down_two_u1_d2,
    'n' : down_two_u1_d1_u1
})
down_two_u2.add_paths({
    'v' : down_two_u2_d1,
    'n' : down_two_u3
})
down_three_u1.add_paths({
    'v' : down_three_u1_d1,
    'n' : down_three_u2
})
down_four.add_paths({
    'v' : down_five,
    'n' : down_four_u1
})

# Trial 2 $2.50
up_week_one = Room("$7.50", "TODAY", "$10", "IN 7 DAYS")

#Trial 3 $1.25
up_week_one_d1 = Room("$6.25", "TODAY", "$10", "IN 7 DAYS")

up_week_two = Room("$8.75", "TODAY", "$10", "IN 7 DAYS")

#Trial 4 $0.625
up_week_one_d1_u1 = Room("$6.88", "TODAY", "$10", "IN 7 DAYS")

up_week_one_d2 = Room("$5.63", "TODAY", "$10", "IN 7 DAYS")

up_week_three = Room("$9.38", "TODAY", "$10", "IN 7 DAYS")

up_week_two_d1 = Room("$8.13", "TODAY", "$10", "IN 7 DAYS")

#Trial 5 $0.3125
up_week_one_d1_u1_d1 = Room("$6.57", "TODAY", "$10", "IN 7 DAYS")
up_week_one_d1_u2 = Room("$7.51", "TODAY", "$10", "IN 7 DAYS")

up_week_one_d2_u1 = Room("$5.94", "TODAY", "$10", "IN 7 DAYS")
up_week_one_d3 = Room("$5.32", "TODAY", "$10", "IN 7 DAYS")

up_week_two_d2 = Room("$7.82", "TODAY", "$10", "IN 7 DAYS")
up_week_two_d1_u1 = Room("$8.44", "TODAY", "$10", "IN 7 DAYS")

up_week_three_d1 = Room("$9.07", "TODAY", "$10", "IN 7 DAYS")
up_week_four = Room("$9.69", "TODAY", "$10", "IN 7 DAYS")

#Finish $0.156
up_week_one_d1_u1_d1_u1 = Room("$6.73", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_one_d1_u1_d2 = Room("$6.41","Task Complete", "IN 7 DAYS", "Thank you")
up_week_one_d1_u3 = Room("$7.67", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_one_d1_u2_d1 = Room("$7.35", "Task Complete", "IN 7 DAYS", "Thank you")

up_week_one_d2_u2 = Room("$6.10", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_one_d2_u1_d1 = Room("$5.78", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_one_d3_u1 = Room("$5.48", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_one_d4 = Room("$5.16", "Task Complete", "IN 7 DAYS", "Thank you")

up_week_two_d2_u1 = Room("$7.98", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_two_d3 = Room("$7.66", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_two_d1_u2 = Room("$8.60", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_two_d1_u1_d1 = Room("$8.28", "Task Complete", "IN 7 DAYS", "Thank you")

up_week_three_d1_u1 = Room("$9.23", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_three_d2 = Room("$8.91", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_four_d1 = Room("$9.53", "Task Complete", "IN 7 DAYS", "Thank you")
up_week_five = Room("$9.85", "Task Complete", "IN 7 DAYS", "Thank you")

#Trial 2 $2.50
down_week_one = Room("$2.50", "TODAY", "$10", "IN 7 DAYS")

#Trial 3  $1.25
down_week_one_u1 = Room("$3.75", "TODAY", "$10", "IN 7 DAYS")
down_week_two = Room("$1.25", "TODAY", "$10", "IN 7 DAYS")

#Trial 4  $0.6250
down_week_one_u2 = Room("$4.38", "TODAY", "$10", "IN 7 DAYS")

down_week_one_u1_d1 = Room("$3.13", "TODAY", "$10", "IN 7 DAYS")

down_week_two_u1 = Room("$1.88", "TODAY", "$10", "IN 7 DAYS")

down_week_three = Room("$0.63", "TODAY", "$10", "IN 7 DAYS")

#Trial 5 $0.3125
down_week_one_u3 = Room("$4.69", "TODAY", "$10", "IN 7 DAYS")
down_week_one_u2_d1 = Room("$4.07", "TODAY", "$10", "IN 7 DAYS")

down_week_one_u1_d2 = Room("$2.82", "TODAY", "$10", "IN 7 DAYS")
down_week_one_u1_d1_u1 = Room("$3.44", "TODAY", "$10", "IN 7 DAYS")

down_week_two_u1_d1 = Room("$1.57", "TODAY", "$10", "IN 7 DAYS")
down_week_two_u2 = Room("$2.19", "TODAY", "$10", "IN 7 DAYS")

down_week_three_u1 = Room("0.94", "TODAY", "$10", "IN 7 DAYS")
down_week_four = Room("$0.31", "TODAY", "$10", "IN 7 DAYS")

#Final $0.156
down_week_one_u4 = Room("$4.85","Task Complete", "IN 7 DAYS", "Thank you")
down_week_one_u3_d1 = Room("$4.53", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_one_u2_d1_u1 = Room("$4.23", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_one_u2_d2 = Room("$3.91", "Task Complete", "IN 7 DAYS", "Thank you")

down_week_one_u1_d2_u1 = Room("$2.98", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_one_u1_d3 = Room("$2.66", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_one_u1_d1_u2 = Room("$3.60","Task Complete", "IN 7 DAYS", "Thank you")
down_week_one_u1_d1_u1_d1 = Room("$3.28", "Task Complete", "IN 7 DAYS", "Thank you")

down_week_two_u1_d1_u1 = Room("$1.73", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_two_u1_d2 = Room("$1.41", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_two_u3 = Room("$2.35", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_two_u2_d1 = Room("$2.03", "Task Complete", "IN 7 DAYS", "Thank you")

down_week_three_u2 = Room("$1.10", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_three_u1_d1 = Room("$0.78", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_four_u1 = Room("$0.47", "Task Complete", "IN 7 DAYS", "Thank you")
down_week_five = Room("$0.15", "Task Complete", "IN 7 DAYS", "Thank you")


#trial 1
central_corridor_2.add_paths({
    'v' : down_week_one,
    'n' : up_week_one
})

#trial 2
up_week_one.add_paths({
    'v' : up_week_one_d1,
    'n' : up_week_two
})

#trial 3
up_week_one_d1.add_paths({
    'v' : up_week_one_d1_u1,
    'n' : up_week_one_d2
})
up_week_two.add_paths({
    'v' : up_week_two_d1,
    'n' : up_week_three
})

#trial 4
up_week_one_d2.add_paths({
    'v' : up_week_one_d2_u1,
    'n' : up_week_one_d3
})
up_week_one_d1_u1.add_paths({
    'v' : up_week_one_d1_u2,
    'n' : up_week_one_d1_u1_d1
})
up_week_two_d1.add_paths({
    'v' : up_week_two_d2,
    'n' : up_week_two_d1_u1
})
up_week_three.add_paths({
    'v' : up_week_three_d1,
    'n' : up_week_four
})

#trial 5
up_week_one_d1_u1_d1.add_paths({
    'v' : up_week_one_d1_u1_d2,
    'n' : up_week_one_d1_u1_d1_u1
}) 
up_week_one_d1_u2.add_paths({
    'v' : up_week_one_d1_u2_d1,
    'n' : up_week_one_d1_u3
}) 
up_week_one_d2_u1.add_paths({
    'v' : up_week_one_d2_u1_d1,
    'n' : up_week_one_d2_u2
}) 
up_week_one_d3.add_paths({
    'v' : up_week_one_d4,
    'n' : up_week_one_d3_u1
}) 
up_week_two_d2.add_paths({
    'v' : up_week_two_d3,
    'n' : up_week_two_d2_u1
}) 
up_week_two_d1_u1.add_paths({
    'v' : up_week_two_d1_u1_d1,
    'n' : up_week_two_d1_u2
}) 
up_week_three_d1.add_paths({
    'v' : up_week_three_d2,
    'n' : up_week_three_d1_u1
})
up_week_four.add_paths({
    'v' : up_week_four_d1,
    'n' : up_week_five
}) 


#trial 2
down_week_one.add_paths({
    'v' : down_week_two,
    'n' : down_week_one_u1
})

#trial 3
down_week_one_u1.add_paths({
    'v' : down_week_one_u1_d1,
    'n' : down_week_one_u2
})
down_week_two.add_paths({
    'v' : down_week_three,
    'n' : down_week_two_u1
})

#trial 4
down_week_one_u2.add_paths({
    'v' : down_week_one_u2_d1,
    'n' : down_week_one_u3
})
down_week_one_u1_d1.add_paths({
    'v' : down_week_one_u1_d2,
    'n' : down_week_one_u1_d1_u1
}) 
down_week_two_u1.add_paths({
    'v' : down_week_two_u1_d1,
    'n' : down_week_two_u2
})
down_week_three.add_paths({
    'v' : down_week_four,
    'n' : down_week_three_u1
})

#trial 5
down_week_one_u3.add_paths({
    'v' : down_week_one_u3_d1,
    'n' : down_week_one_u4
}) 
down_week_one_u2_d1.add_paths({
    'v' : down_week_one_u2_d2,
    'n' : down_week_one_u2_d1_u1
}) 
down_week_one_u1_d2.add_paths({
    'v' : down_week_one_u1_d3,
    'n' : down_week_one_u1_d2_u1
}) 
down_week_one_u1_d1_u1.add_paths({
    'v' : down_week_one_u1_d1_u1_d1,
    'n' : down_week_one_u1_d1_u2
}) 
down_week_two_u1_d1.add_paths({
    'v' : down_week_two_u1_d2,
    'n' : down_week_two_u1_d1_u1
})
down_week_two_u2.add_paths({
    'v' : down_week_two_u2_d1,
    'n' : down_week_two_u3
})
down_week_three_u1.add_paths({
    'v' : down_week_three_u1_d1,
    'n' : down_week_three_u2
})
down_week_four.add_paths({
    'v' : down_week_five,
    'n' : down_week_four_u1
})

# Trial 2 $2.50
up_month_one = Room("$7.50", "TODAY", "$10", "IN 30 DAYS")

#Trial 3 $1.25
up_month_one_d1 = Room("$6.25", "TODAY", "$10", "IN 30 DAYS")

up_month_two = Room("$8.75", "TODAY", "$10", "IN 30 DAYS")

#Trial 4 $0.625
up_month_one_d1_u1 = Room("$6.88", "TODAY", "$10", "IN 30 DAYS")

up_month_one_d2 = Room("$5.63", "TODAY", "$10", "IN 30 DAYS")

up_month_three = Room("$9.38", "TODAY", "$10", "IN 30 DAYS")

up_month_two_d1 = Room("$8.13", "TODAY", "$10", "IN 30 DAYS")

#Trial 5 $0.3125
up_month_one_d1_u1_d1 = Room("$6.57", "TODAY", "$10", "IN 30 DAYS")
up_month_one_d1_u2 = Room("$7.51", "TODAY", "$10", "IN 30 DAYS")

up_month_one_d2_u1 = Room("$5.94", "TODAY", "$10", "IN 30 DAYS")
up_month_one_d3 = Room("$5.32", "TODAY", "$10", "IN 30 DAYS")

up_month_two_d2 = Room("$7.82", "TODAY", "$10", "IN 30 DAYS")
up_month_two_d1_u1 = Room("$8.44", "TODAY", "$10", "IN 30 DAYS")

up_month_three_d1 = Room("$9.07", "TODAY", "$10", "IN 30 DAYS")
up_month_four = Room("$9.69", "TODAY", "$10", "IN 30 DAYS")

#Finish $0.156
up_month_one_d1_u1_d1_u1 = Room("$6.73", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_one_d1_u1_d2 = Room("$6.41","Task Complete", "IN 30 DAYS", "Thank you")
up_month_one_d1_u3 = Room("$7.67", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_one_d1_u2_d1 = Room("$7.35", "Task Complete", "IN 30 DAYS", "Thank you")

up_month_one_d2_u2 = Room("$6.10", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_one_d2_u1_d1 = Room("$5.78", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_one_d3_u1 = Room("$5.48", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_one_d4 = Room("$5.16", "Task Complete", "IN 30 DAYS", "Thank you")

up_month_two_d2_u1 = Room("$7.98", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_two_d3 = Room("$7.66", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_two_d1_u2 = Room("$8.60", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_two_d1_u1_d1 = Room("$8.28", "Task Complete", "IN 30 DAYS", "Thank you")

up_month_three_d1_u1 = Room("$9.23", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_three_d2 = Room("$8.91", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_four_d1 = Room("$9.53", "Task Complete", "IN 30 DAYS", "Thank you")
up_month_five = Room("$9.85", "Task Complete", "IN 30 DAYS", "Thank you")

#Trial 2 $2.50
down_month_one = Room("$2.50", "TODAY", "$10", "IN 30 DAYS")

#Trial 3  $1.25
down_month_one_u1 = Room("$3.75", "TODAY", "$10", "IN 30 DAYS")
down_month_two = Room("$1.25", "TODAY", "$10", "IN 30 DAYS")

#Trial 4  $0.6250
down_month_one_u2 = Room("$4.38", "TODAY", "$10", "IN 30 DAYS")

down_month_one_u1_d1 = Room("$3.13", "TODAY", "$10", "IN 30 DAYS")

down_month_two_u1 = Room("$1.88", "TODAY", "$10", "IN 30 DAYS")

down_month_three = Room("$0.63", "TODAY", "$10", "IN 30 DAYS")

#Trial 5 $0.3125
down_month_one_u3 = Room("$4.69", "TODAY", "$10", "IN 30 DAYS")
down_month_one_u2_d1 = Room("$4.07", "TODAY", "$10", "IN 30 DAYS")

down_month_one_u1_d2 = Room("$2.82", "TODAY", "$10", "IN 30 DAYS")
down_month_one_u1_d1_u1 = Room("$3.44", "TODAY", "$10", "IN 30 DAYS")

down_month_two_u1_d1 = Room("$1.57", "TODAY", "$10", "IN 30 DAYS")
down_month_two_u2 = Room("$2.19", "TODAY", "$10", "IN 30 DAYS")

down_month_three_u1 = Room("0.94", "TODAY", "$10", "IN 30 DAYS")
down_month_four = Room("$0.31", "TODAY", "$10", "IN 30 DAYS")

#Final $0.156
down_month_one_u4 = Room("$4.85","Task Complete", "IN 30 DAYS", "Thank you")
down_month_one_u3_d1 = Room("$4.53", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_one_u2_d1_u1 = Room("$4.23", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_one_u2_d2 = Room("$3.91", "Task Complete", "IN 30 DAYS", "Thank you")

down_month_one_u1_d2_u1 = Room("$2.98", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_one_u1_d3 = Room("$2.66", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_one_u1_d1_u2 = Room("$3.60","Task Complete", "IN 30 DAYS", "Thank you")
down_month_one_u1_d1_u1_d1 = Room("$3.28", "Task Complete", "IN 30 DAYS", "Thank you")

down_month_two_u1_d1_u1 = Room("$1.73", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_two_u1_d2 = Room("$1.41", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_two_u3 = Room("$2.35", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_two_u2_d1 = Room("$2.03", "Task Complete", "IN 30 DAYS", "Thank you")

down_month_three_u2 = Room("$1.10", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_three_u1_d1 = Room("$0.78", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_four_u1 = Room("$0.47", "Task Complete", "IN 30 DAYS", "Thank you")
down_month_five = Room("$0.15", "Task Complete", "IN 30 DAYS", "Thank you")


#trial 1
central_corridor_3.add_paths({
    'v' : down_month_one,
    'n' : up_month_one
})

#trial 2
up_month_one.add_paths({
    'v' : up_month_one_d1,
    'n' : up_month_two
})

#trial 3
up_month_one_d1.add_paths({
    'v' : up_month_one_d1_u1,
    'n' : up_month_one_d2
})
up_month_two.add_paths({
    'v' : up_month_two_d1,
    'n' : up_month_three
})

#trial 4
up_month_one_d2.add_paths({
    'v' : up_month_one_d2_u1,
    'n' : up_month_one_d3
})
up_month_one_d1_u1.add_paths({
    'v' : up_month_one_d1_u2,
    'n' : up_month_one_d1_u1_d1
})
up_month_two_d1.add_paths({
    'v' : up_month_two_d2,
    'n' : up_month_two_d1_u1
})
up_month_three.add_paths({
    'v' : up_month_three_d1,
    'n' : up_month_four
})

#trial 5
up_month_one_d1_u1_d1.add_paths({
    'v' : up_month_one_d1_u1_d2,
    'n' : up_month_one_d1_u1_d1_u1
}) 
up_month_one_d1_u2.add_paths({
    'v' : up_month_one_d1_u2_d1,
    'n' : up_month_one_d1_u3
}) 
up_month_one_d2_u1.add_paths({
    'v' : up_month_one_d2_u1_d1,
    'n' : up_month_one_d2_u2
}) 
up_month_one_d3.add_paths({
    'v' : up_month_one_d4,
    'n' : up_month_one_d3_u1
}) 
up_month_two_d2.add_paths({
    'v' : up_month_two_d3,
    'n' : up_month_two_d2_u1
}) 
up_month_two_d1_u1.add_paths({
    'v' : up_month_two_d1_u1_d1,
    'n' : up_month_two_d1_u2
}) 
up_month_three_d1.add_paths({
    'v' : up_month_three_d2,
    'n' : up_month_three_d1_u1
})
up_month_four.add_paths({
    'v' : up_month_four_d1,
    'n' : up_month_five
}) 


#trial 2
down_month_one.add_paths({
    'v' : down_month_two,
    'n' : down_month_one_u1
})

#trial 3
down_month_one_u1.add_paths({
    'v' : down_month_one_u1_d1,
    'n' : down_month_one_u2
})
down_month_two.add_paths({
    'v' : down_month_three,
    'n' : down_month_two_u1
})

#trial 4
down_month_one_u2.add_paths({
    'v' : down_month_one_u2_d1,
    'n' : down_month_one_u3
})
down_month_one_u1_d1.add_paths({
    'v' : down_month_one_u1_d2,
    'n' : down_month_one_u1_d1_u1
}) 
down_month_two_u1.add_paths({
    'v' : down_month_two_u1_d1,
    'n' : down_month_two_u2
})
down_month_three.add_paths({
    'v' : down_month_four,
    'n' : down_month_three_u1
})

#trial 5
down_month_one_u3.add_paths({
    'v' : down_month_one_u3_d1,
    'n' : down_month_one_u4
}) 
down_month_one_u2_d1.add_paths({
    'v' : down_month_one_u2_d2,
    'n' : down_month_one_u2_d1_u1
}) 
down_month_one_u1_d2.add_paths({
    'v' : down_month_one_u1_d3,
    'n' : down_month_one_u1_d2_u1
}) 
down_month_one_u1_d1_u1.add_paths({
    'v' : down_month_one_u1_d1_u1_d1,
    'n' : down_month_one_u1_d1_u2
}) 
down_month_two_u1_d1.add_paths({
    'v' : down_month_two_u1_d2,
    'n' : down_month_two_u1_d1_u1
})
down_month_two_u2.add_paths({
    'v' : down_month_two_u2_d1,
    'n' : down_month_two_u3
})
down_month_three_u1.add_paths({
    'v' : down_month_three_u1_d1,
    'n' : down_month_three_u2
})
down_month_four.add_paths({
    'v' : down_month_five,
    'n' : down_month_four_u1
})

# Trial 2 $2.50
up_6_months_one = Room("$7.50", "TODAY", "$10", "IN 180 DAYS")

#Trial 3 $1.25
up_6_months_one_d1 = Room("$6.25", "TODAY", "$10", "IN 180 DAYS")

up_6_months_two = Room("$8.75", "TODAY", "$10", "IN 180 DAYS")

#Trial 4 $0.625
up_6_months_one_d1_u1 = Room("$6.88", "TODAY", "$10", "IN 180 DAYS")

up_6_months_one_d2 = Room("$5.63", "TODAY", "$10", "IN 180 DAYS")

up_6_months_three = Room("$9.38", "TODAY", "$10", "IN 180 DAYS")

up_6_months_two_d1 = Room("$8.13", "TODAY", "$10", "IN 180 DAYS")

#Trial 5 $0.3125
up_6_months_one_d1_u1_d1 = Room("$6.57", "TODAY", "$10", "IN 180 DAYS")
up_6_months_one_d1_u2 = Room("$7.51", "TODAY", "$10", "IN 180 DAYS")

up_6_months_one_d2_u1 = Room("$5.94", "TODAY", "$10", "IN 180 DAYS")
up_6_months_one_d3 = Room("$5.32", "TODAY", "$10", "IN 180 DAYS")

up_6_months_two_d2 = Room("$7.82", "TODAY", "$10", "IN 180 DAYS")
up_6_months_two_d1_u1 = Room("$8.44", "TODAY", "$10", "IN 180 DAYS")

up_6_months_three_d1 = Room("$9.07", "TODAY", "$10", "IN 180 DAYS")
up_6_months_four = Room("$9.69", "TODAY", "$10", "IN 180 DAYS")

#Finish $0.156
up_6_months_one_d1_u1_d1_u1 = Room("$6.73", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_one_d1_u1_d2 = Room("$6.41","Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_one_d1_u3 = Room("$7.67", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_one_d1_u2_d1 = Room("$7.35", "Task Complete", "IN 180 DAYS", "Thank you")

up_6_months_one_d2_u2 = Room("$6.10", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_one_d2_u1_d1 = Room("$5.78", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_one_d3_u1 = Room("$5.48", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_one_d4 = Room("$5.16", "Task Complete", "IN 180 DAYS", "Thank you")

up_6_months_two_d2_u1 = Room("$7.98", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_two_d3 = Room("$7.66", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_two_d1_u2 = Room("$8.60", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_two_d1_u1_d1 = Room("$8.28", "Task Complete", "IN 180 DAYS", "Thank you")

up_6_months_three_d1_u1 = Room("$9.23", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_three_d2 = Room("$8.91", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_four_d1 = Room("$9.53", "Task Complete", "IN 180 DAYS", "Thank you")
up_6_months_five = Room("$9.85", "Task Complete", "IN 180 DAYS", "Thank you")

#Trial 2 $2.50
down_6_months_one = Room("$2.50", "TODAY", "$10", "IN 180 DAYS")

#Trial 3  $1.25
down_6_months_one_u1 = Room("$3.75", "TODAY", "$10", "IN 180 DAYS")
down_6_months_two = Room("$1.25", "TODAY", "$10", "IN 180 DAYS")

#Trial 4  $0.6250
down_6_months_one_u2 = Room("$4.38", "TODAY", "$10", "IN 180 DAYS")

down_6_months_one_u1_d1 = Room("$3.13", "TODAY", "$10", "IN 180 DAYS")

down_6_months_two_u1 = Room("$1.88", "TODAY", "$10", "IN 180 DAYS")

down_6_months_three = Room("$0.63", "TODAY", "$10", "IN 180 DAYS")

#Trial 5 $0.3125
down_6_months_one_u3 = Room("$4.69", "TODAY", "$10", "IN 180 DAYS")
down_6_months_one_u2_d1 = Room("$4.07", "TODAY", "$10", "IN 180 DAYS")

down_6_months_one_u1_d2 = Room("$2.82", "TODAY", "$10", "IN 180 DAYS")
down_6_months_one_u1_d1_u1 = Room("$3.44", "TODAY", "$10", "IN 180 DAYS")

down_6_months_two_u1_d1 = Room("$1.57", "TODAY", "$10", "IN 180 DAYS")
down_6_months_two_u2 = Room("$2.19", "TODAY", "$10", "IN 180 DAYS")

down_6_months_three_u1 = Room("0.94", "TODAY", "$10", "IN 180 DAYS")
down_6_months_four = Room("$0.31", "TODAY", "$10", "IN 180 DAYS")

#Final $0.156
down_6_months_one_u4 = Room("$4.85","Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_one_u3_d1 = Room("$4.53", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_one_u2_d1_u1 = Room("$4.23", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_one_u2_d2 = Room("$3.91", "Task Complete", "IN 180 DAYS", "Thank you")

down_6_months_one_u1_d2_u1 = Room("$2.98", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_one_u1_d3 = Room("$2.66", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_one_u1_d1_u2 = Room("$3.60","Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_one_u1_d1_u1_d1 = Room("$3.28", "Task Complete", "IN 180 DAYS", "Thank you")

down_6_months_two_u1_d1_u1 = Room("$1.73", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_two_u1_d2 = Room("$1.41", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_two_u3 = Room("$2.35", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_two_u2_d1 = Room("$2.03", "Task Complete", "IN 180 DAYS", "Thank you")

down_6_months_three_u2 = Room("$1.10", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_three_u1_d1 = Room("$0.78", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_four_u1 = Room("$0.47", "Task Complete", "IN 180 DAYS", "Thank you")
down_6_months_five = Room("$0.15", "Task Complete", "IN 180 DAYS", "Thank you")


#trial 1
central_corridor_4.add_paths({
    'v' : down_6_months_one,
    'n' : up_6_months_one
})

#trial 2
up_6_months_one.add_paths({
    'v' : up_6_months_one_d1,
    'n' : up_6_months_two
})

#trial 3
up_6_months_one_d1.add_paths({
    'v' : up_6_months_one_d1_u1,
    'n' : up_6_months_one_d2
})
up_6_months_two.add_paths({
    'v' : up_6_months_two_d1,
    'n' : up_6_months_three
})

#trial 4
up_6_months_one_d2.add_paths({
    'v' : up_6_months_one_d2_u1,
    'n' : up_6_months_one_d3
})
up_6_months_one_d1_u1.add_paths({
    'v' : up_6_months_one_d1_u2,
    'n' : up_6_months_one_d1_u1_d1
})
up_6_months_two_d1.add_paths({
    'v' : up_6_months_two_d2,
    'n' : up_6_months_two_d1_u1
})
up_6_months_three.add_paths({
    'v' : up_6_months_three_d1,
    'n' : up_6_months_four
})

#trial 5
up_6_months_one_d1_u1_d1.add_paths({
    'v' : up_6_months_one_d1_u1_d2,
    'n' : up_6_months_one_d1_u1_d1_u1
}) 
up_6_months_one_d1_u2.add_paths({
    'v' : up_6_months_one_d1_u2_d1,
    'n' : up_6_months_one_d1_u3
}) 
up_6_months_one_d2_u1.add_paths({
    'v' : up_6_months_one_d2_u1_d1,
    'n' : up_6_months_one_d2_u2
}) 
up_6_months_one_d3.add_paths({
    'v' : up_6_months_one_d4,
    'n' : up_6_months_one_d3_u1
}) 
up_6_months_two_d2.add_paths({
    'v' : up_6_months_two_d3,
    'n' : up_6_months_two_d2_u1
}) 
up_6_months_two_d1_u1.add_paths({
    'v' : up_6_months_two_d1_u1_d1,
    'n' : up_6_months_two_d1_u2
}) 
up_6_months_three_d1.add_paths({
    'v' : up_6_months_three_d2,
    'n' : up_6_months_three_d1_u1
})
up_6_months_four.add_paths({
    'v' : up_6_months_four_d1,
    'n' : up_6_months_five
}) 


#trial 2
down_6_months_one.add_paths({
    'v' : down_6_months_two,
    'n' : down_6_months_one_u1
})

#trial 3
down_6_months_one_u1.add_paths({
    'v' : down_6_months_one_u1_d1,
    'n' : down_6_months_one_u2
})
down_6_months_two.add_paths({
    'v' : down_6_months_three,
    'n' : down_6_months_two_u1
})

#trial 4
down_6_months_one_u2.add_paths({
    'v' : down_6_months_one_u2_d1,
    'n' : down_6_months_one_u3
})
down_6_months_one_u1_d1.add_paths({
    'v' : down_6_months_one_u1_d2,
    'n' : down_6_months_one_u1_d1_u1
}) 
down_6_months_two_u1.add_paths({
    'v' : down_6_months_two_u1_d1,
    'n' : down_6_months_two_u2
})
down_6_months_three.add_paths({
    'v' : down_6_months_four,
    'n' : down_6_months_three_u1
})

#trial 5
down_6_months_one_u3.add_paths({
    'v' : down_6_months_one_u3_d1,
    'n' : down_6_months_one_u4
}) 
down_6_months_one_u2_d1.add_paths({
    'v' : down_6_months_one_u2_d2,
    'n' : down_6_months_one_u2_d1_u1
}) 
down_6_months_one_u1_d2.add_paths({
    'v' : down_6_months_one_u1_d3,
    'n' : down_6_months_one_u1_d2_u1
}) 
down_6_months_one_u1_d1_u1.add_paths({
    'v' : down_6_months_one_u1_d1_u1_d1,
    'n' : down_6_months_one_u1_d1_u2
}) 
down_6_months_two_u1_d1.add_paths({
    'v' : down_6_months_two_u1_d2,
    'n' : down_6_months_two_u1_d1_u1
})
down_6_months_two_u2.add_paths({
    'v' : down_6_months_two_u2_d1,
    'n' : down_6_months_two_u3
})
down_6_months_three_u1.add_paths({
    'v' : down_6_months_three_u1_d1,
    'n' : down_6_months_three_u2
})
down_6_months_four.add_paths({
    'v' : down_6_months_five,
    'n' : down_6_months_four_u1
})

# Trial 2 $2.50
up_year_one = Room("$7.50", "TODAY", "$10", "IN 365 DAYS")

#Trial 3 $1.25
up_year_one_d1 = Room("$6.25", "TODAY", "$10", "IN 365 DAYS")

up_year_two = Room("$8.75", "TODAY", "$10", "IN 365 DAYS")

#Trial 4 $0.625
up_year_one_d1_u1 = Room("$6.88", "TODAY", "$10", "IN 365 DAYS")

up_year_one_d2 = Room("$5.63", "TODAY", "$10", "IN 365 DAYS")

up_year_three = Room("$9.38", "TODAY", "$10", "IN 365 DAYS")

up_year_two_d1 = Room("$8.13", "TODAY", "$10", "IN 365 DAYS")

#Trial 5 $0.3125
up_year_one_d1_u1_d1 = Room("$6.57", "TODAY", "$10", "IN 365 DAYS")
up_year_one_d1_u2 = Room("$7.51", "TODAY", "$10", "IN 365 DAYS")

up_year_one_d2_u1 = Room("$5.94", "TODAY", "$10", "IN 365 DAYS")
up_year_one_d3 = Room("$5.32", "TODAY", "$10", "IN 365 DAYS")

up_year_two_d2 = Room("$7.82", "TODAY", "$10", "IN 365 DAYS")
up_year_two_d1_u1 = Room("$8.44", "TODAY", "$10", "IN 365 DAYS")

up_year_three_d1 = Room("$9.07", "TODAY", "$10", "IN 365 DAYS")
up_year_four = Room("$9.69", "TODAY", "$10", "IN 365 DAYS")

#Finish $0.156
up_year_one_d1_u1_d1_u1 = Room("$6.73", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_one_d1_u1_d2 = Room("$6.41","Task Complete", "IN 365 DAYS", "Thank you")
up_year_one_d1_u3 = Room("$7.67", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_one_d1_u2_d1 = Room("$7.35", "Task Complete", "IN 365 DAYS", "Thank you")

up_year_one_d2_u2 = Room("$6.10", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_one_d2_u1_d1 = Room("$5.78", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_one_d3_u1 = Room("$5.48", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_one_d4 = Room("$5.16", "Task Complete", "IN 365 DAYS", "Thank you")

up_year_two_d2_u1 = Room("$7.98", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_two_d3 = Room("$7.66", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_two_d1_u2 = Room("$8.60", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_two_d1_u1_d1 = Room("$8.28", "Task Complete", "IN 365 DAYS", "Thank you")

up_year_three_d1_u1 = Room("$9.23", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_three_d2 = Room("$8.91", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_four_d1 = Room("$9.53", "Task Complete", "IN 365 DAYS", "Thank you")
up_year_five = Room("$9.85", "Task Complete", "IN 365 DAYS", "Thank you")

#Trial 2 $2.50
down_year_one = Room("$2.50", "TODAY", "$10", "IN 365 DAYS")

#Trial 3  $1.25
down_year_one_u1 = Room("$3.75", "TODAY", "$10", "IN 365 DAYS")
down_year_two = Room("$1.25", "TODAY", "$10", "IN 365 DAYS")

#Trial 4  $0.6250
down_year_one_u2 = Room("$4.38", "TODAY", "$10", "IN 365 DAYS")

down_year_one_u1_d1 = Room("$3.13", "TODAY", "$10", "IN 365 DAYS")

down_year_two_u1 = Room("$1.88", "TODAY", "$10", "IN 365 DAYS")

down_year_three = Room("$0.63", "TODAY", "$10", "IN 365 DAYS")

#Trial 5 $0.3125
down_year_one_u3 = Room("$4.69", "TODAY", "$10", "IN 365 DAYS")
down_year_one_u2_d1 = Room("$4.07", "TODAY", "$10", "IN 365 DAYS")

down_year_one_u1_d2 = Room("$2.82", "TODAY", "$10", "IN 365 DAYS")
down_year_one_u1_d1_u1 = Room("$3.44", "TODAY", "$10", "IN 365 DAYS")

down_year_two_u1_d1 = Room("$1.57", "TODAY", "$10", "IN 365 DAYS")
down_year_two_u2 = Room("$2.19", "TODAY", "$10", "IN 365 DAYS")

down_year_three_u1 = Room("0.94", "TODAY", "$10", "IN 365 DAYS")
down_year_four = Room("$0.31", "TODAY", "$10", "IN 365 DAYS")

#Final $0.156
down_year_one_u4 = Room("$4.85","Task Complete", "IN 365 DAYS", "Thank you")
down_year_one_u3_d1 = Room("$4.53", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_one_u2_d1_u1 = Room("$4.23", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_one_u2_d2 = Room("$3.91", "Task Complete", "IN 365 DAYS", "Thank you")

down_year_one_u1_d2_u1 = Room("$2.98", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_one_u1_d3 = Room("$2.66", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_one_u1_d1_u2 = Room("$3.60","Task Complete", "IN 365 DAYS", "Thank you")
down_year_one_u1_d1_u1_d1 = Room("$3.28", "Task Complete", "IN 365 DAYS", "Thank you")

down_year_two_u1_d1_u1 = Room("$1.73", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_two_u1_d2 = Room("$1.41", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_two_u3 = Room("$2.35", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_two_u2_d1 = Room("$2.03", "Task Complete", "IN 365 DAYS", "Thank you")

down_year_three_u2 = Room("$1.10", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_three_u1_d1 = Room("$0.78", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_four_u1 = Room("$0.47", "Task Complete", "IN 365 DAYS", "Thank you")
down_year_five = Room("$0.15", "Task Complete", "IN 365 DAYS", "Thank you")


#trial 1
central_corridor_5.add_paths({
    'v' : down_year_one,
    'n' : up_year_one
})

#trial 2
up_year_one.add_paths({
    'v' : up_year_one_d1,
    'n' : up_year_two
})

#trial 3
up_year_one_d1.add_paths({
    'v' : up_year_one_d1_u1,
    'n' : up_year_one_d2
})
up_year_two.add_paths({
    'v' : up_year_two_d1,
    'n' : up_year_three
})

#trial 4
up_year_one_d2.add_paths({
    'v' : up_year_one_d2_u1,
    'n' : up_year_one_d3
})
up_year_one_d1_u1.add_paths({
    'v' : up_year_one_d1_u2,
    'n' : up_year_one_d1_u1_d1
})
up_year_two_d1.add_paths({
    'v' : up_year_two_d2,
    'n' : up_year_two_d1_u1
})
up_year_three.add_paths({
    'v' : up_year_three_d1,
    'n' : up_year_four
})

#trial 5
up_year_one_d1_u1_d1.add_paths({
    'v' : up_year_one_d1_u1_d2,
    'n' : up_year_one_d1_u1_d1_u1
}) 
up_year_one_d1_u2.add_paths({
    'v' : up_year_one_d1_u2_d1,
    'n' : up_year_one_d1_u3
}) 
up_year_one_d2_u1.add_paths({
    'v' : up_year_one_d2_u1_d1,
    'n' : up_year_one_d2_u2
}) 
up_year_one_d3.add_paths({
    'v' : up_year_one_d4,
    'n' : up_year_one_d3_u1
}) 
up_year_two_d2.add_paths({
    'v' : up_year_two_d3,
    'n' : up_year_two_d2_u1
}) 
up_year_two_d1_u1.add_paths({
    'v' : up_year_two_d1_u1_d1,
    'n' : up_year_two_d1_u2
}) 
up_year_three_d1.add_paths({
    'v' : up_year_three_d2,
    'n' : up_year_three_d1_u1
})
up_year_four.add_paths({
    'v' : up_year_four_d1,
    'n' : up_year_five
}) 


#trial 2
down_year_one.add_paths({
    'v' : down_year_two,
    'n' : down_year_one_u1
})

#trial 3
down_year_one_u1.add_paths({
    'v' : down_year_one_u1_d1,
    'n' : down_year_one_u2
})
down_year_two.add_paths({
    'v' : down_year_three,
    'n' : down_year_two_u1
})

#trial 4
down_year_one_u2.add_paths({
    'v' : down_year_one_u2_d1,
    'n' : down_year_one_u3
})
down_year_one_u1_d1.add_paths({
    'v' : down_year_one_u1_d2,
    'n' : down_year_one_u1_d1_u1
}) 
down_year_two_u1.add_paths({
    'v' : down_year_two_u1_d1,
    'n' : down_year_two_u2
})
down_year_three.add_paths({
    'v' : down_year_four,
    'n' : down_year_three_u1
})

#trial 5
down_year_one_u3.add_paths({
    'v' : down_year_one_u3_d1,
    'n' : down_year_one_u4
}) 
down_year_one_u2_d1.add_paths({
    'v' : down_year_one_u2_d2,
    'n' : down_year_one_u2_d1_u1
}) 
down_year_one_u1_d2.add_paths({
    'v' : down_year_one_u1_d3,
    'n' : down_year_one_u1_d2_u1
}) 
down_year_one_u1_d1_u1.add_paths({
    'v' : down_year_one_u1_d1_u1_d1,
    'n' : down_year_one_u1_d1_u2
}) 
down_year_two_u1_d1.add_paths({
    'v' : down_year_two_u1_d2,
    'n' : down_year_two_u1_d1_u1
})
down_year_two_u2.add_paths({
    'v' : down_year_two_u2_d1,
    'n' : down_year_two_u3
})
down_year_three_u1.add_paths({
    'v' : down_year_three_u1_d1,
    'n' : down_year_three_u2
})
down_year_four.add_paths({
    'v' : down_year_five,
    'n' : down_year_four_u1
})

# Trial 2 $2.50
up_5_years_one = Room("$7.50", "TODAY", "$10", "IN 1825 DAYS")

#Trial 3 $1.25
up_5_years_one_d1 = Room("$6.25", "TODAY", "$10", "IN 1825 DAYS")

up_5_years_two = Room("$8.75", "TODAY", "$10", "IN 1825 DAYS")

#Trial 4 $0.625
up_5_years_one_d1_u1 = Room("$6.88", "TODAY", "$10", "IN 1825 DAYS")

up_5_years_one_d2 = Room("$5.63", "TODAY", "$10", "IN 1825 DAYS")

up_5_years_three = Room("$9.38", "TODAY", "$10", "IN 1825 DAYS")

up_5_years_two_d1 = Room("$8.13", "TODAY", "$10", "IN 1825 DAYS")

#Trial 5 $0.3125
up_5_years_one_d1_u1_d1 = Room("$6.57", "TODAY", "$10", "IN 1825 DAYS")
up_5_years_one_d1_u2 = Room("$7.51", "TODAY", "$10", "IN 1825 DAYS")

up_5_years_one_d2_u1 = Room("$5.94", "TODAY", "$10", "IN 1825 DAYS")
up_5_years_one_d3 = Room("$5.32", "TODAY", "$10", "IN 1825 DAYS")

up_5_years_two_d2 = Room("$7.82", "TODAY", "$10", "IN 1825 DAYS")
up_5_years_two_d1_u1 = Room("$8.44", "TODAY", "$10", "IN 1825 DAYS")

up_5_years_three_d1 = Room("$9.07", "TODAY", "$10", "IN 1825 DAYS")
up_5_years_four = Room("$9.69", "TODAY", "$10", "IN 1825 DAYS")

#Finish $0.156
up_5_years_one_d1_u1_d1_u1 = Room("$6.73", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_one_d1_u1_d2 = Room("$6.41","Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_one_d1_u3 = Room("$7.67", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_one_d1_u2_d1 = Room("$7.35", "Task Complete", "IN 1825 DAYS", "Thank you")

up_5_years_one_d2_u2 = Room("$6.10", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_one_d2_u1_d1 = Room("$5.78", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_one_d3_u1 = Room("$5.48", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_one_d4 = Room("$5.16", "Task Complete", "IN 1825 DAYS", "Thank you")

up_5_years_two_d2_u1 = Room("$7.98", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_two_d3 = Room("$7.66", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_two_d1_u2 = Room("$8.60", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_two_d1_u1_d1 = Room("$8.28", "Task Complete", "IN 1825 DAYS", "Thank you")

up_5_years_three_d1_u1 = Room("$9.23", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_three_d2 = Room("$8.91", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_four_d1 = Room("$9.53", "Task Complete", "IN 1825 DAYS", "Thank you")
up_5_years_five = Room("$9.85", "Task Complete", "IN 1825 DAYS", "Thank you")

#Trial 2 $2.50
down_5_years_one = Room("$2.50", "TODAY", "$10", "IN 1825 DAYS")

#Trial 3  $1.25
down_5_years_one_u1 = Room("$3.75", "TODAY", "$10", "IN 1825 DAYS")
down_5_years_two = Room("$1.25", "TODAY", "$10", "IN 1825 DAYS")

#Trial 4  $0.6250
down_5_years_one_u2 = Room("$4.38", "TODAY", "$10", "IN 1825 DAYS")

down_5_years_one_u1_d1 = Room("$3.13", "TODAY", "$10", "IN 1825 DAYS")

down_5_years_two_u1 = Room("$1.88", "TODAY", "$10", "IN 1825 DAYS")

down_5_years_three = Room("$0.63", "TODAY", "$10", "IN 1825 DAYS")

#Trial 5 $0.3125
down_5_years_one_u3 = Room("$4.69", "TODAY", "$10", "IN 1825 DAYS")
down_5_years_one_u2_d1 = Room("$4.07", "TODAY", "$10", "IN 1825 DAYS")

down_5_years_one_u1_d2 = Room("$2.82", "TODAY", "$10", "IN 1825 DAYS")
down_5_years_one_u1_d1_u1 = Room("$3.44", "TODAY", "$10", "IN 1825 DAYS")

down_5_years_two_u1_d1 = Room("$1.57", "TODAY", "$10", "IN 1825 DAYS")
down_5_years_two_u2 = Room("$2.19", "TODAY", "$10", "IN 1825 DAYS")

down_5_years_three_u1 = Room("0.94", "TODAY", "$10", "IN 1825 DAYS")
down_5_years_four = Room("$0.31", "TODAY", "$10", "IN 1825 DAYS")

#Final $0.156
down_5_years_one_u4 = Room("$4.85","Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_one_u3_d1 = Room("$4.53", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_one_u2_d1_u1 = Room("$4.23", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_one_u2_d2 = Room("$3.91", "Task Complete", "IN 1825 DAYS", "Thank you")

down_5_years_one_u1_d2_u1 = Room("$2.98", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_one_u1_d3 = Room("$2.66", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_one_u1_d1_u2 = Room("$3.60","Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_one_u1_d1_u1_d1 = Room("$3.28", "Task Complete", "IN 1825 DAYS", "Thank you")

down_5_years_two_u1_d1_u1 = Room("$1.73", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_two_u1_d2 = Room("$1.41", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_two_u3 = Room("$2.35", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_two_u2_d1 = Room("$2.03", "Task Complete", "IN 1825 DAYS", "Thank you")

down_5_years_three_u2 = Room("$1.10", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_three_u1_d1 = Room("$0.78", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_four_u1 = Room("$0.47", "Task Complete", "IN 1825 DAYS", "Thank you")
down_5_years_five = Room("$0.15", "Task Complete", "IN 1825 DAYS", "Thank you")


#trial 1
central_corridor_6.add_paths({
    'v' : down_5_years_one,
    'n' : up_5_years_one
})

#trial 2
up_5_years_one.add_paths({
    'v' : up_5_years_one_d1,
    'n' : up_5_years_two
})

#trial 3
up_5_years_one_d1.add_paths({
    'v' : up_5_years_one_d1_u1,
    'n' : up_5_years_one_d2
})
up_5_years_two.add_paths({
    'v' : up_5_years_two_d1,
    'n' : up_5_years_three
})

#trial 4
up_5_years_one_d2.add_paths({
    'v' : up_5_years_one_d2_u1,
    'n' : up_5_years_one_d3
})
up_5_years_one_d1_u1.add_paths({
    'v' : up_5_years_one_d1_u2,
    'n' : up_5_years_one_d1_u1_d1
})
up_5_years_two_d1.add_paths({
    'v' : up_5_years_two_d2,
    'n' : up_5_years_two_d1_u1
})
up_5_years_three.add_paths({
    'v' : up_5_years_three_d1,
    'n' : up_5_years_four
})

#trial 5
up_5_years_one_d1_u1_d1.add_paths({
    'v' : up_5_years_one_d1_u1_d2,
    'n' : up_5_years_one_d1_u1_d1_u1
}) 
up_5_years_one_d1_u2.add_paths({
    'v' : up_5_years_one_d1_u2_d1,
    'n' : up_5_years_one_d1_u3
}) 
up_5_years_one_d2_u1.add_paths({
    'v' : up_5_years_one_d2_u1_d1,
    'n' : up_5_years_one_d2_u2
}) 
up_5_years_one_d3.add_paths({
    'v' : up_5_years_one_d4,
    'n' : up_5_years_one_d3_u1
}) 
up_5_years_two_d2.add_paths({
    'v' : up_5_years_two_d3,
    'n' : up_5_years_two_d2_u1
}) 
up_5_years_two_d1_u1.add_paths({
    'v' : up_5_years_two_d1_u1_d1,
    'n' : up_5_years_two_d1_u2
}) 
up_5_years_three_d1.add_paths({
    'v' : up_5_years_three_d2,
    'n' : up_5_years_three_d1_u1
})
up_5_years_four.add_paths({
    'v' : up_5_years_four_d1,
    'n' : up_5_years_five
}) 


#trial 2
down_5_years_one.add_paths({
    'v' : down_5_years_two,
    'n' : down_5_years_one_u1
})

#trial 3
down_5_years_one_u1.add_paths({
    'v' : down_5_years_one_u1_d1,
    'n' : down_5_years_one_u2
})
down_5_years_two.add_paths({
    'v' : down_5_years_three,
    'n' : down_5_years_two_u1
})

#trial 4
down_5_years_one_u2.add_paths({
    'v' : down_5_years_one_u2_d1,
    'n' : down_5_years_one_u3
})
down_5_years_one_u1_d1.add_paths({
    'v' : down_5_years_one_u1_d2,
    'n' : down_5_years_one_u1_d1_u1
}) 
down_5_years_two_u1.add_paths({
    'v' : down_5_years_two_u1_d1,
    'n' : down_5_years_two_u2
})
down_5_years_three.add_paths({
    'v' : down_5_years_four,
    'n' : down_5_years_three_u1
})

#trial 5
down_5_years_one_u3.add_paths({
    'v' : down_5_years_one_u3_d1,
    'n' : down_5_years_one_u4
}) 
down_5_years_one_u2_d1.add_paths({
    'v' : down_5_years_one_u2_d2,
    'n' : down_5_years_one_u2_d1_u1
}) 
down_5_years_one_u1_d2.add_paths({
    'v' : down_5_years_one_u1_d3,
    'n' : down_5_years_one_u1_d2_u1
}) 
down_5_years_one_u1_d1_u1.add_paths({
    'v' : down_5_years_one_u1_d1_u1_d1,
    'n' : down_5_years_one_u1_d1_u2
}) 
down_5_years_two_u1_d1.add_paths({
    'v' : down_5_years_two_u1_d2,
    'n' : down_5_years_two_u1_d1_u1
})
down_5_years_two_u2.add_paths({
    'v' : down_5_years_two_u2_d1,
    'n' : down_5_years_two_u3
})
down_5_years_three_u1.add_paths({
    'v' : down_5_years_three_u1_d1,
    'n' : down_5_years_three_u2
})
down_5_years_four.add_paths({
    'v' : down_5_years_five,
    'n' : down_5_years_four_u1
})

# Trial 2 $2.50
up_25_years_one = Room("$7.50", "TODAY", "$10", "IN 9125 DAYS")

#Trial 3 $1.25
up_25_years_one_d1 = Room("$6.25", "TODAY", "$10", "IN 9125 DAYS")

up_25_years_two = Room("$8.75", "TODAY", "$10", "IN 9125 DAYS")

#Trial 4 $0.625
up_25_years_one_d1_u1 = Room("$6.88", "TODAY", "$10", "IN 9125 DAYS")

up_25_years_one_d2 = Room("$5.63", "TODAY", "$10", "IN 9125 DAYS")

up_25_years_three = Room("$9.38", "TODAY", "$10", "IN 9125 DAYS")

up_25_years_two_d1 = Room("$8.13", "TODAY", "$10", "IN 9125 DAYS")

#Trial 5 $0.3125
up_25_years_one_d1_u1_d1 = Room("$6.57", "TODAY", "$10", "IN 9125 DAYS")
up_25_years_one_d1_u2 = Room("$7.51", "TODAY", "$10", "IN 9125 DAYS")

up_25_years_one_d2_u1 = Room("$5.94", "TODAY", "$10", "IN 9125 DAYS")
up_25_years_one_d3 = Room("$5.32", "TODAY", "$10", "IN 9125 DAYS")

up_25_years_two_d2 = Room("$7.82", "TODAY", "$10", "IN 9125 DAYS")
up_25_years_two_d1_u1 = Room("$8.44", "TODAY", "$10", "IN 9125 DAYS")

up_25_years_three_d1 = Room("$9.07", "TODAY", "$10", "IN 9125 DAYS")
up_25_years_four = Room("$9.69", "TODAY", "$10", "IN 9125 DAYS")

#Finish $0.156
up_25_years_one_d1_u1_d1_u1 = Room("$6.73", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_one_d1_u1_d2 = Room("$6.41","Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_one_d1_u3 = Room("$7.67", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_one_d1_u2_d1 = Room("$7.35", "Task Complete", "IN 9125 DAYS", "Thank you")

up_25_years_one_d2_u2 = Room("$6.10", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_one_d2_u1_d1 = Room("$5.78", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_one_d3_u1 = Room("$5.48", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_one_d4 = Room("$5.16", "Task Complete", "IN 9125 DAYS", "Thank you")

up_25_years_two_d2_u1 = Room("$7.98", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_two_d3 = Room("$7.66", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_two_d1_u2 = Room("$8.60", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_two_d1_u1_d1 = Room("$8.28", "Task Complete", "IN 9125 DAYS", "Thank you")

up_25_years_three_d1_u1 = Room("$9.23", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_three_d2 = Room("$8.91", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_four_d1 = Room("$9.53", "Task Complete", "IN 9125 DAYS", "Thank you")
up_25_years_five = Room("$9.85", "Task Complete", "IN 9125 DAYS", "Thank you")

#Trial 2 $2.50
down_25_years_one = Room("$2.50", "TODAY", "$10", "IN 9125 DAYS")

#Trial 3  $1.25
down_25_years_one_u1 = Room("$3.75", "TODAY", "$10", "IN 9125 DAYS")
down_25_years_two = Room("$1.25", "TODAY", "$10", "IN 9125 DAYS")

#Trial 4  $0.6250
down_25_years_one_u2 = Room("$4.38", "TODAY", "$10", "IN 9125 DAYS")

down_25_years_one_u1_d1 = Room("$3.13", "TODAY", "$10", "IN 9125 DAYS")

down_25_years_two_u1 = Room("$1.88", "TODAY", "$10", "IN 9125 DAYS")

down_25_years_three = Room("$0.63", "TODAY", "$10", "IN 9125 DAYS")

#Trial 5 $0.3125
down_25_years_one_u3 = Room("$4.69", "TODAY", "$10", "IN 9125 DAYS")
down_25_years_one_u2_d1 = Room("$4.07", "TODAY", "$10", "IN 9125 DAYS")

down_25_years_one_u1_d2 = Room("$2.82", "TODAY", "$10", "IN 9125 DAYS")
down_25_years_one_u1_d1_u1 = Room("$3.44", "TODAY", "$10", "IN 9125 DAYS")

down_25_years_two_u1_d1 = Room("$1.57", "TODAY", "$10", "IN 9125 DAYS")
down_25_years_two_u2 = Room("$2.19", "TODAY", "$10", "IN 9125 DAYS")

down_25_years_three_u1 = Room("0.94", "TODAY", "$10", "IN 9125 DAYS")
down_25_years_four = Room("$0.31", "TODAY", "$10", "IN 9125 DAYS")

#Final $0.156
down_25_years_one_u4 = Room("$4.85","Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_one_u3_d1 = Room("$4.53", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_one_u2_d1_u1 = Room("$4.23", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_one_u2_d2 = Room("$3.91", "Task Complete", "IN 9125 DAYS", "Thank you")

down_25_years_one_u1_d2_u1 = Room("$2.98", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_one_u1_d3 = Room("$2.66", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_one_u1_d1_u2 = Room("$3.60","Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_one_u1_d1_u1_d1 = Room("$3.28", "Task Complete", "IN 9125 DAYS", "Thank you")

down_25_years_two_u1_d1_u1 = Room("$1.73", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_two_u1_d2 = Room("$1.41", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_two_u3 = Room("$2.35", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_two_u2_d1 = Room("$2.03", "Task Complete", "IN 9125 DAYS", "Thank you")

down_25_years_three_u2 = Room("$1.10", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_three_u1_d1 = Room("$0.78", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_four_u1 = Room("$0.47", "Task Complete", "IN 9125 DAYS", "Thank you")
down_25_years_five = Room("$0.15", "Task Complete", "IN 9125 DAYS", "Thank you")


#trial 1
central_corridor_7.add_paths({
    'v' : down_25_years_one,
    'n' : up_25_years_one
})

#trial 2
up_25_years_one.add_paths({
    'v' : up_25_years_one_d1,
    'n' : up_25_years_two
})

#trial 3
up_25_years_one_d1.add_paths({
    'v' : up_25_years_one_d1_u1,
    'n' : up_25_years_one_d2
})
up_25_years_two.add_paths({
    'v' : up_25_years_two_d1,
    'n' : up_25_years_three
})

#trial 4
up_25_years_one_d2.add_paths({
    'v' : up_25_years_one_d2_u1,
    'n' : up_25_years_one_d3
})
up_25_years_one_d1_u1.add_paths({
    'v' : up_25_years_one_d1_u2,
    'n' : up_25_years_one_d1_u1_d1
})
up_25_years_two_d1.add_paths({
    'v' : up_25_years_two_d2,
    'n' : up_25_years_two_d1_u1
})
up_25_years_three.add_paths({
    'v' : up_25_years_three_d1,
    'n' : up_25_years_four
})

#trial 5
up_25_years_one_d1_u1_d1.add_paths({
    'v' : up_25_years_one_d1_u1_d2,
    'n' : up_25_years_one_d1_u1_d1_u1
}) 
up_25_years_one_d1_u2.add_paths({
    'v' : up_25_years_one_d1_u2_d1,
    'n' : up_25_years_one_d1_u3
}) 
up_25_years_one_d2_u1.add_paths({
    'v' : up_25_years_one_d2_u1_d1,
    'n' : up_25_years_one_d2_u2
}) 
up_25_years_one_d3.add_paths({
    'v' : up_25_years_one_d4,
    'n' : up_25_years_one_d3_u1
}) 
up_25_years_two_d2.add_paths({
    'v' : up_25_years_two_d3,
    'n' : up_25_years_two_d2_u1
}) 
up_25_years_two_d1_u1.add_paths({
    'v' : up_25_years_two_d1_u1_d1,
    'n' : up_25_years_two_d1_u2
}) 
up_25_years_three_d1.add_paths({
    'v' : up_25_years_three_d2,
    'n' : up_25_years_three_d1_u1
})
up_25_years_four.add_paths({
    'v' : up_25_years_four_d1,
    'n' : up_25_years_five
}) 


#trial 2
down_25_years_one.add_paths({
    'v' : down_25_years_two,
    'n' : down_25_years_one_u1
})

#trial 3
down_25_years_one_u1.add_paths({
    'v' : down_25_years_one_u1_d1,
    'n' : down_25_years_one_u2
})
down_25_years_two.add_paths({
    'v' : down_25_years_three,
    'n' : down_25_years_two_u1
})

#trial 4
down_25_years_one_u2.add_paths({
    'v' : down_25_years_one_u2_d1,
    'n' : down_25_years_one_u3
})
down_25_years_one_u1_d1.add_paths({
    'v' : down_25_years_one_u1_d2,
    'n' : down_25_years_one_u1_d1_u1
}) 
down_25_years_two_u1.add_paths({
    'v' : down_25_years_two_u1_d1,
    'n' : down_25_years_two_u2
})
down_25_years_three.add_paths({
    'v' : down_25_years_four,
    'n' : down_25_years_three_u1
})

#trial 5
down_25_years_one_u3.add_paths({
    'v' : down_25_years_one_u3_d1,
    'n' : down_25_years_one_u4
}) 
down_25_years_one_u2_d1.add_paths({
    'v' : down_25_years_one_u2_d2,
    'n' : down_25_years_one_u2_d1_u1
}) 
down_25_years_one_u1_d2.add_paths({
    'v' : down_25_years_one_u1_d3,
    'n' : down_25_years_one_u1_d2_u1
}) 
down_25_years_one_u1_d1_u1.add_paths({
    'v' : down_25_years_one_u1_d1_u1_d1,
    'n' : down_25_years_one_u1_d1_u2
}) 
down_25_years_two_u1_d1.add_paths({
    'v' : down_25_years_two_u1_d2,
    'n' : down_25_years_two_u1_d1_u1
})
down_25_years_two_u2.add_paths({
    'v' : down_25_years_two_u2_d1,
    'n' : down_25_years_two_u3
})
down_25_years_three_u1.add_paths({
    'v' : down_25_years_three_u1_d1,
    'n' : down_25_years_three_u2
})
down_25_years_four.add_paths({
    'v' : down_25_years_five,
    'n' : down_25_years_four_u1
})

START = central_corridor
reSTART = central_corridor_2
reSTART_2 = central_corridor_3
reSTART_3 = central_corridor_4
reSTART_4 = central_corridor_5
reSTART_5 = central_corridor_6
reSTART_6 = central_corridor_7
