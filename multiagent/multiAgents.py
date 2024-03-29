# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # Tinh khoang cach tu vi tri hien tai toi thuc an
        foodsDistance = newFood.asList()
        # Sap xep lai mang thuc an theo thu tu khoang cach
        foodsDistance = sorted(foodsDistance, key = lambda position: manhattanDistance(newPos, position))
        closestFoodDistance = -1
        if len(foodsDistance) > 0:
                closestFoodDistance = manhattanDistance(newPos, foodsDistance[0])

        # Tinh khoang cach tu vi tri hien tai toi con ma va kiem tra nhung vi tri xung quanh con ma
        closestGhostDistance = 1
        proximityToGhost = 0
        for ghostState in successorGameState.getGhostPositions():
            distance = manhattanDistance(newPos, ghostState)
            closestGhostDistance += distance
            if distance <= 1:
                proximityToGhost += 1
        """In ra cac khoang cach """
        #tuple_distance = (closestFoodDistance, closestGhostDistance, proximityToGhost)
        #print(tuple_distance)
        return successorGameState.getScore() + (1 / float(closestFoodDistance)) - (1 / float(closestGhostDistance)) - proximityToGhost
def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        numGhosts = gameState.getNumAgents() - 1
        return self.maximize(gameState, 1, numGhosts)

    def maximize(self, gameState, depth, numGhosts):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        maxValue = float('-inf')
        bestAction = Directions.STOP
        for action in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, action)
            tempValue = self.minimize(successor, depth, 1,  numGhosts)
            if tempValue > maxValue:
                maxValue = tempValue
                bestAction = action

        if depth > 1:
            return maxValue
        return bestAction

    def minimize(self, gameState, depth, agentIndex, numGhosts):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        minValue = float('inf')
        for action in gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == numGhosts:
                if depth < self.depth:
                    minValue = min(minValue, self.maximize(successor, depth + 1, numGhosts))
                else:
                    minValue = min(minValue, self.evaluationFunction(successor))
            else:
                minValue = min(minValue, self.minimize(successor, depth, agentIndex + 1, numGhosts))

        return minValue
#util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        numGhosts = gameState.getNumAgents() - 1
        return self.maximize(gameState, 1, numGhosts, float('-inf'), float('inf'))

    def maximize(self, gameState, depth, numGhosts, alpha, beta):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        maxValue = float('-inf')
        bestAction = Directions.STOP
        for action in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, action)
            tempValue = self.minimize(successor, depth, 1,  numGhosts, alpha, beta)
            if maxValue < tempValue:
                maxValue = tempValue
                bestAction = action
            # Loai bo nhanh
            if maxValue > beta:
                return maxValue
            alpha = max(maxValue, alpha)

        if depth > 1:
            return maxValue
        return bestAction

    def minimize(self, gameState, depth, agentIndex, numGhosts, alpha, beta):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        minValue = float('inf')

        for action in gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == numGhosts:
                if depth < self.depth:
                    minValue = min(minValue, self.maximize(successor, depth + 1, numGhosts, alpha, beta))
                else:
                    minValue = min(minValue, self.evaluationFunction(successor))
            else:
                minValue = min(minValue, self.minimize(successor, depth, agentIndex + 1, numGhosts, alpha, beta))
            # Loai bo nhanh
            if minValue < alpha:
                return minValue
            beta = min(beta, minValue)
        return minValue


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
#        util.raiseNotDefined()
        numGhosts = gameState.getNumAgents() - 1
        return self.maximize(gameState, 1, numGhosts)

    def maximize(self, gameState, depth, numGhosts):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        maxValue = float('-inf')
        bestAction = Directions.STOP
        for action in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, action)
            tempValue = self.getExpectValue(successor, depth, 1, numGhosts)

            if maxValue < tempValue:
                maxValue = tempValue
                bestAction = action

        if depth > 1:
            return maxValue
        return bestAction

    def getExpectValue(self, gameState, depth, agentIndex, numGhosts):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        expectValue = 0
        legalActions = gameState.getLegalActions(agentIndex)
        successor_probability = 1.0/len(legalActions) # xac suat

        for action in legalActions:
            successor = gameState.generateSuccessor(agentIndex, action)
            if agentIndex == numGhosts:
                if depth < self.depth:
                    expectValue += successor_probability * self.maximize(successor, depth + 1, numGhosts)
                else:
                    expectValue += successor_probability * self.evaluationFunction(successor)
            else:
                expectValue += successor_probability * self.getExpectValue(successor, depth, agentIndex + 1, numGhosts)
        return expectValue



def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    # Tinh khoang cach den cac thuc an
    pacmanPosition = currentGameState.getPacmanPosition()
    foods = currentGameState.getFood()
    closestFoodDistance = -1
    foodsPosition = foods.asList()
    foodsPosition = sorted(foodsPosition, key = lambda position: manhattanDistance(position, pacmanPosition))
    if len(foodsPosition) > 0:
        closestFoodDistance = manhattanDistance(foodsPosition[0], pacmanPosition)

    # Tinh khoang cach den con ma
    distanceToGhost = 1
    proximityToGhost = 0

    for ghostState in currentGameState.getGhostStates():
        distance = manhattanDistance(pacmanPosition, ghostState.getPosition())
        distanceToGhost += distance
        if distance <= 1:
            proximityToGhost += 1

    # An nhung cai capsule de vo hieu hoa con ma
    newCapsules = currentGameState.getCapsules()
    numberOfCapsules = len(newCapsules)

    # tuple_distance = (closestFoodDistance, distanceToGhost, proximityToGhost, numberOfCapsules)
    # print(tuple_distance)
    return currentGameState.getScore() + (1 / float(closestFoodDistance)) - (1 / float(distanceToGhost)) - proximityToGhost - numberOfCapsules

# Abbreviation
better = betterEvaluationFunction

