⚙️ LangChain Runnables – Advanced AI Workflow Components
========================================================

This repository demonstrates how to use **LangChain Runnables** to build highly composable, modular, and scalable AI pipelines.

Runnables are core building blocks in LangChain that make it easier to **compose**, **branch**, **combine**, and **manipulate** the flow of data through different AI components. They're like functional pipelines that allow you to **chain logic and models** together cleanly.


🧠 What Are Runnables?
----------------------

In LangChain, **runnables** are the standard interface for **defining unit tasks** and composing them. A Runnable takes input, performs a task (like calling a model or applying logic), and returns output. The beauty of this system lies in its **composability**—you can nest, branch, and parallelize tasks easily.

🔄 Types of Runnables Covered
-----------------------------

### 1️⃣ RunnableSequence

*   Executes multiple steps **in order**, passing output of one as input to the next.
    
*   Think of it like a **pipeline** or function composition.
    

**Use case**: Preprocess → Prompt → Parse → Output.

### 2️⃣ RunnableParallel

*   Runs multiple tasks **simultaneously** on the same input.
    
*   Great for **multitask applications**, like extracting sentiment, summary, and tags from the same text.
    

### 3️⃣ RunnableBranch

*   Implements conditional logic.
    
*   Routes input to different branches based on some rule or function.
    

**Use case**: If user query is about resume → go to resume parser; else → use default chat model.

### 4️⃣ RunnableLambda

*   Lets you insert any **custom Python function** inside a chain.
    
*   Useful for **quick transformations, filtering, or decision logic** without creating separate classes.
    

### 5️⃣ RunnablePassthrough

*   Does nothing but passes the input forward.
    
*   Useful as a placeholder in chains or for testing intermediate steps.
    

🧪 Why Use Runnables?
---------------------

*   ✅ Clean code for complex chains
    
*   ✅ Declarative and composable logic
    
*   ✅ Easy to test and debug
    
*   ✅ Works with LangGraph and LangServe
