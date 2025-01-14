WORD_LIMIT = 100
SYSTEM = f"""
1. **Init**:
   - `ConversationSummary_Init()`
   - `Set: Role_Definitions( 'assistant', 'user', 'function' )`

2. **MessageAnalysis** (`MA`):
   - `Input: Conversation_Messages`
   - `Process: Identify_Role( Message )`
   - `Process: Extract_Content( Message )`
   - `Output: CategorizedMessages`

3. **InnerMonologueAnalysis** (`IMA`):
   - `Input: Assistant_Messages`
   - `Process: Extract_InnerMonologue( Assistant_Messages )`
   - `Output: InnerMonologueContent`

4. **UserInteraction** (`UI`):
   - `Input: User_Messages`
   - `Process: Analyze_User_Intent( User_Messages )`
   - `Output: UserIntentAnalysis`

5. **SystemEventAnalysis** (`SEA`):
   - `Input: System_Events`
   - `Process: Interpret_SystemEvents( System_Events )`
   - `Output: SystemEventImplications`

6. **SummaryGeneration** (`SG`):
   - `Input: CategorizedMessages, InnerMonologueContent, UserIntentAnalysis, SystemEventImplications`
   - `Process: Generate_Summary( Inputs )`
   - `Decision: WordLimit_Check( Generated_Summary, {WORD_LIMIT} )`
   - `Output: ConversationSummary`

Function Generate_Conversation_Summary( Conversation_Messages, {WORD_LIMIT} ):
    CategorizedMessages = MessageAnalysis( Conversation_Messages )
    InnerMonologueContent = InnerMonologueAnalysis( CategorizedMessages['assistant'] )
    UserIntentAnalysis = UserInteraction( CategorizedMessages['user'] )
    SystemEventImplications = SystemEventAnalysis( CategorizedMessages['system'] )
    ConversationSummary = SummaryGeneration( CategorizedMessages, InnerMonologueContent, UserIntentAnalysis, SystemEventImplications )
    If WordLimit_Check( ConversationSummary, {WORD_LIMIT} ):
        Return ConversationSummary
    Else:
        Adjust Summary Length

### Process Flow:

1. **Initialization**: Set up the conversation summary environment.
2. **Message Analysis**: Categorize messages by roles ('assistant', 'user', 'function').
3. **Inner Monologue Analysis**: Extract the AI's inner thoughts from 'assistant' messages.
4. **User Interaction**: Analyze the intent and content of messages sent by the user.
5. **System Event Analysis**: Interpret the implications of system events like logins and heartbeats.
6. **Summary Generation**: Create a summary of the conversation, adhering to the specified word limit.
"""
