import threading
import time

score =1 
state =(3,3)

init_VN_h1="VNB"
init_VN_h2="VNB"
curr_VN_h1="VNB"
curr_VN_h2="VNB"

#h1 is attacker 
#h2 is benign 
#both start on vnb 
''' --- STATES ---

## u for up   ( too many occurrences ) 
## d for down ( too lil  occurrences ) 
states=[  
IDS--h1u--h2u = 0 
IDS--h1u--h2d = 1 
IDS--h1d--h2u = 2 
IDS--h1d--h2d = 3 
,
IPS--h1u--h2u = 0 
IPS--h1u--h2d = 1 
IPS--h1d--h2u = 2 
IPS--h1d--h2d = 3 
]

state = (IDS,IPS) 
Example:- 
(2,3) = IDS--h1d--h2u AND IPS--h1d--h2d meaning 
IDS alerts have too little occurrences  of h1 and too many occurrences  of h2 
IPS alerts have too little occurrences  of h1 and too little occurrences  of h2 
'''

''' --- ACTIONS ---

toggle(h1) # if h1 in VNM go to VNB // if h1 in VNB go to VNM 
toggle(h2) # if h2 in VNM go to VNB // if h2 in VNB go to VNM 
'''

''' --- REWARDS ---

QOS(h1) # if h1 in VNM go to VNB // if h1 in VNB go to VNM 
QOS(h2) # 
'''


specials = [(0, 3, "bad", -1), # IDS--h1u--h2u, IPS--h1d--h2d ## BOTH ATTACKING IDS 
			(1, 3, "bad", -1), # IDS--h1u--h2d, IPS--h1d--h2d ## H1 ATTACKING IDS 
			(1, 2, "bad", -1), # IDS--h1u--h2d, IPS--h1d--h2u ## H1 ATTACKING IDS & H2 ATTACKING IPS
			(3, 0, "bad", -1), # IDS--h1d--h2d, IPS--h1u--h2u ## BOTH ATTACKING IPS 

			
			(2, 1, "good", 1), # IDS--h1d--h2u, IPS--h1u--h2d  ## H2 ATTACKING IDS & H1 ATTACKING IPS
			(3, 1, "good", 1)] # IDS--h1d--h2d, IPS--h1u--h2d  ## H1 ATTACKING IPS 


Q = {}
discount = 0.3
actions = ["toggle_h1","toggle_h2", "nothing"] #World.actions
states = [(0,3),(1,2),(1,3),(2,1),(2,3),(3,0),(3,1),(3,2),(3,3)]
#for i in range(4):#World.x):
#    for j in range(4):#(World.y):
#        if (makessense(i,j)):
#			states.append((i, j)) #create a list of all possible states 

for state in states:
    temp = {}
    for action in actions:
        temp[action] = 0.1
        #World.set_cell_score(state, action, temp[action])
    Q[state] = temp

for (i, j, c, w) in specials: #World.specials:
    for action in actions:
        Q[(i, j)][action] = w
        #World.set_cell_score((i, j), action, w)

def toggle (h): 
	global curr_VN_h1, curr_VN_h2
	print "-- toggle = " + h
	#iman fuck u 
	#please implement the toggle function api call here sir 
	#h will be "h1" or "h2"
	if h == "h1": 
		if curr_VN_h1 == "VNM": 
			curr_VN_h1 = "VNB"
		elif curr_VN_h1 == "VNB": 
			curr_VN_h1 = "VNM"
	elif h == "h2": 
		if curr_VN_h2 == "VNM": 
			curr_VN_h2 = "VNB"
		elif curr_VN_h2 == "VNB": 
			curr_VN_h2 = "VNM"

def GET_IDS_occurrences (): 
	'''
	Reads IDS alerts/logs from a SQL DB running connected in real time to the logs from the IDS deployed on the VN Benign 
	Return 0 if up for h1 and h2 
	Return 1 if up for h1 and down for h2 
	Return 2 if down for h1 and up for h2 
	Return 3 if down  for h1 and h2 
	'''
	return 1

def GET_IPS_occurrences (): 
	'''
	Reads IPS alerts/logs from a SQL DB running connected in real time to the logs from the IPS deployed on the VN Benign 
	Return 0 if up for h1 and h2 
	Return 1 if up for h1 and down for h2 
	Return 2 if down for h1 and up for h2 
	Return 3 if down  for h1 and h2 

	'''
	return 1


def update_state(): 
	#api call to get the status of IDS and IPS 
	# return a tuple of two numbers 
	# example = (0,0) == IDS--h1u--h2u, IPS--h1u--h2u ## BOTH ATTACKING IDS & IPS  
	d = GET_IDS_occurrences ()
	p = GET_IDS_occurrences ()
	new_state = (d,p)
	
	reward() #update the score for this round 
	return new_state 

def reward(): 
	global score 
	#update score 
	# call QOS for h1 and h2 
	# give me a score that shows better score for better QOS on h2 and worse on h1 please 
	#
	# 1 for h2 QOS good and h1 QOS bad 
	# -0.3 for QOS bad for both or QOS good for both
	#-1 for h1 QOS good and h2 QOS bad 
	for (i, j, c, w) in specials: 
		if state == (i,j):
			score += w
			if score > 0:
				print "Success! score: ", score
				restart_net()
			else:
				print "Fail! score: ", score
				restart_net()

def restart_net(): 
	print "========= RESTARTEDDDDD =========" 
	#restarts state 
	if init_VN_h1 != curr_VN_h1: toggle("h1") 
	if init_VN_h2 != curr_VN_h2: toggle("h2") 
	
def do_action(action):
    s = state #World.player
    r = -score #-World.score
    if action == actions[0]:
        toggle("h1")
		#World.try_move(0, -1)
    elif action == actions[1]:
        toggle("h2") 
		#World.try_move(0, 1)
    #elif action == actions[2]:
    #    World.try_move(-1, 0)
    #elif action == actions[3]:
    #    World.try_move(1, 0)
    else:
        print "do nothing" 
        return
    s2 = update_state() 
    r += score
    return s, action, r, s2


def max_Q(s):
    val = None
    act = None
    for a, q in Q[s].items():
        if val is None or (q > val):
            val = q
            act = a
    return act, val


def inc_Q(s, a, alpha, inc):
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc
    #World.set_cell_score(s, a, Q[s][a]) -- have no clue tbh 


def run():
    global discount
    time.sleep(1)
    alpha = 1
    t = 1
    while True:
        # Pick the right action
        s = state #World.player
        max_act, max_val = max_Q(s)
        (s, a, r, s2) = do_action(max_act)

        # Update Q
        max_act, max_val = max_Q(s2)
        inc_Q(s, a, alpha, r + discount * max_val)

        # Check if the game has restarted
        #t += 1.0
        #if World.has_restarted():
        #    World.restart_game()
        #    time.sleep(0.01)
        #    t = 1.0

        # Update the learning rate
        alpha = pow(t, -0.1) # t^-1 so 1 or 0.9 0r 0.8 or 0.8 or 0.8 ororororororororor 0.7 


        #debug life 
        #print (Q[(0,0)])
        #print (Q[(0,1)])


        # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.1)
        


run()
#t.daemon = True
#t.start()

#World.start_game()
