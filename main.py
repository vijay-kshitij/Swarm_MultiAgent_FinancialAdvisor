from swarm import Swarm, Agent  # Import the Swarm framework and Agent class for multi-agent orchestration
from dotenv import load_dotenv  # Load environment variables from a .env file
from tavily import TavilyClient  # Import TavilyClient for web searches using the Tavily API
import os  # Import os for environment variable access

# Load environment variables from a .env file
load_dotenv()

# Initialize the Swarm client
client = Swarm()

# Initialize TavilyClient with the API key from .env file
tavily_client = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))


def web_search(query):
    # Perform the search using TavilyClient and return the result
    print("Transferring to the Researcher")
    print(f"Performing web search for: {query}")
    return tavily_client.search(query)

def budget_management():
    # Transferring to an agent for some budget management tips
    print("Transferring to Budget Management Agent")
    return budget


def suggest_investments():
    # Transferring to an agent for some investment suggestions
    print("Transferring to the Investment Advisor")
    return investment

def book_recommender():
    # Transferring to an agent for some Finance Book Recommendations
    print("Transferring to the Book Recommender")
    return book_recommender


# Delegates tasks to the appropriate specialized agents
manager = Agent(
    name="Financial Manager",
    instructions="""
    You oversee the financial process and delegate tasks to your team.
    If you don't know how to answer a question or need more information, call on the Researcher Agent 
    to perform a web search.
    """,
    functions=[budget_management, suggest_investments, book_recommender, web_search],
)


# suggests budgeting strategies
budget = Agent(
    name="Budgeting Agent",
    instructions="""
    As the Budgeting Agent, you are responsible for guiding users in creating, tracking, 
    and optimizing their budgets. Your key role is to provide clear, actionable strategies based on the input data 
    the user has provided (such as financial data, spending patterns) to help them achieve 
    financial stability and maximize savings.

    You must offer practical recommendations that align with the user's financial goals, 
    lifestyle, and priorities. When necessary, advise on adjustments to spending habits 
    and allocation of resources to ensure they stay within budget while addressing 
    essential expenses and savings objectives.
    """,
    functions=[budget_management]
)

# Provides recommendations for investment
investment = Agent(
    name="Investment Advisor",
    instructions="""As the Investment Advisor, your primary responsibility is to provide clients with tailored 
    investment recommendations based on the user input. 
    
    Focus on maximizing  growth while minimizing risk, and maintain a forward-looking approach to anticipate changes 
    in the financial landscape.

    Always prioritize the client's best interests, offering clear and transparent advice to help 
    them make informed decisions.
    """,
    functions=[suggest_investments]
)

# Recommends finance books or articles
book_recommender = Agent(
    name="Book Recommender",
    instructions="""
    As the Book Recommender, your primary responsibility is to suggest finance-related books and 
    articles that align with the user's interests, learning goals, and current knowledge level.

    You should provide recommendations based on the user's specific inquiries or expressed preferences, 
    offering resources that cover topics such as investment strategies, personal finance management, 
    wealth building, or economic trends.

    Always aim to suggest well-reviewed and reputable books or articles that provide valuable insights 
    and practical guidance to help users enhance their financial literacy and achieve their financial objectives.
    """,
    function=[book_recommender]
)

# Handles web searches using the Tavily API when the other agents cannot answer a question.
research = Agent(
    name="Researcher",
    instructions="You perform web searches to gather relevant information for the team",
    function=[web_search],
)

# Main Loop
while True:
    user_input = input("Enter your question: ")

    response = client.run(
        agent=manager,
        messages=[{"role": "user", "content": user_input}]
    )

    print("Final Response: ")
    print(response.messages[-1]["content"])
    print()

