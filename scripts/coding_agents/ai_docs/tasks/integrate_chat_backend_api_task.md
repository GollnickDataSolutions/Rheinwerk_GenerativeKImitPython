# AI Task Planning Template

## 1. Task Title
Integrate REST API Backend for Chat Interface

## 2. Task Overview
Replace the mock/demo chat functionality in the existing chat modal with real backend integration. The chat interface should connect to the Search API endpoint (`https://gollnickdatarag.azurewebsites.net/api/rag`) to provide actual responses to user queries. This will transform the chat from a demo interface into a fully functional conversational system.

## 3. Project Analysis

### Project Context
- **Current State:** The portfolio website (`index.html`) already has a fully functional chat modal UI with avatar button, modal dialog, message display area, and input field. Currently, the chat uses a mock response that simulates bot replies after a 500ms delay.
- **Relevant Codebase:** 
  - `scripts/coding_agents/index.html` - Contains the complete chat interface implementation
  - `scripts/coding_agents/ai_docs/templates/api_description.md` - Documents the REST API endpoint and response format
  - The chat modal is already styled and functional, only needs backend integration
  - Current mock implementation is in the `sendMessage()` function around line 539-550

### Dependencies & Constraints
- **Required Libraries/APIs:** 
  - REST API endpoint: `https://gollnickdatarag.azurewebsites.net/api/rag`
  - Uses query parameter `query` with URL-encoded user messages
  - Returns JSON response with `answer` field
- **Constraints:** 
  - Must maintain existing UI/UX design and styling
  - Should handle API errors gracefully without breaking the chat interface
  - Must properly encode query parameters for URL safety
  - Should provide user feedback during API calls (loading states)
  - Must work with existing modal and message display structure
  - Should maintain accessibility features already implemented

## 4. Context & Problem Definition
- **Background:** The chat interface was previously implemented as a UI-only feature with mock responses. To make it functional, it needs to connect to the actual backend Search API that provides RAG (Retrieval-Augmented Generation) capabilities for answering user queries.
- **The Problem:** 
  - Current `sendMessage()` function uses `setTimeout()` to simulate bot responses
  - Need to replace mock response with actual HTTP request to the REST API
  - Must properly encode user input as URL query parameter
  - Need to parse JSON response and extract the `answer` field
  - Should handle network errors, API errors, and loading states
  - Must maintain smooth user experience during API calls

## 5. Technical Requirements
- **Platform/Environment:** 
  - Modern web browsers with Fetch API support
  - Vanilla JavaScript (ES6+)
  - No external libraries required (use native `fetch()` API)
- **Key Functionality:** 
  - Send user messages to REST API endpoint via GET request
  - Properly URL-encode query parameters
  - Parse JSON response and extract answer
  - Display API responses as bot messages
  - Handle loading states (show loading indicator or message)
  - Handle errors gracefully (network errors, API errors, invalid responses)
  - Maintain existing message display format
- **Performance:** 
  - API calls should not block UI (use async/await)
  - Loading feedback should appear immediately
  - Response time depends on API, but UI should remain responsive
- **Security:** 
  - Properly encode user input to prevent URL injection
  - Handle CORS if applicable (API should allow requests from website origin)
  - No sensitive data handling required for this task

## 6. API & Backend Changes
### New Endpoints
*No backend changes required - using existing endpoint:*
- `GET https://gollnickdatarag.azurewebsites.net/api/rag?query=<encoded_query>` - Search API endpoint

### Database Schema Changes
*No database changes required*

### Logic/Business Rules
*No backend logic changes required - using existing API*

## 7. Frontend Changes
- **UI Components:** 
  - Chat Messages Area: Already exists, will display API responses
  - Chat Input: Already exists, will send messages to API
  - Loading Indicator: May need to add visual feedback during API calls (e.g., "Thinking..." message or spinner)
- **User Flow:** 
  1. User types message and clicks Send or presses Enter
  2. User message appears in chat (existing functionality)
  3. Loading indicator appears (new - shows API call in progress)
  4. API request is sent to backend with encoded query
  5. API response is received and parsed
  6. Bot response appears in chat with answer from API
  7. If error occurs, error message is displayed to user
- **State Management:** 
  - Track loading state to show/hide loading indicator
  - Handle API call state (idle, loading, success, error)
  - Maintain existing message array/display logic

## 8. Implementation Plan
### Step 1: Planning & Design
1. Review API endpoint structure and response format from `api_description.md`
2. Design error handling strategy (network errors, API errors, invalid responses)
3. Design loading state UI (simple text message or consider adding spinner)
4. Plan URL encoding approach (use `encodeURIComponent()`)
5. Review existing `sendMessage()` function structure
6. Plan async/await implementation pattern

### Step 2: Backend Implementation
*No backend implementation required - using existing API*

### Step 3: Frontend Implementation
1. Modify `sendMessage()` function in `index.html`:
   - Remove mock `setTimeout()` response
   - Add async function to call API endpoint
   - Implement proper URL encoding for query parameter
   - Use `fetch()` API to make GET request
   - Parse JSON response
   - Extract `answer` field from response
   - Display answer as bot message
2. Add loading state handling:
   - Show loading message when API call starts
   - Remove loading message when response arrives
   - Consider adding "Thinking..." or similar message
3. Add error handling:
   - Try-catch block around API call
   - Handle network errors (fetch failures)
   - Handle API errors (non-200 status codes)
   - Handle invalid JSON responses
   - Display user-friendly error messages
4. Ensure proper async/await usage:
   - Make `sendMessage()` async
   - Use await for API call
   - Handle promises correctly

### Step 4: Integration & Testing
1. Test successful API calls with various queries
2. Test URL encoding with special characters, spaces, and non-ASCII characters
3. Test error handling (simulate network failures, invalid responses)
4. Test loading states (verify loading message appears/disappears correctly)
5. Test message display (user messages and bot responses appear correctly)
6. Test input clearing after sending message
7. Test multiple consecutive messages
8. Verify existing modal functionality still works (open/close, keyboard shortcuts)
9. Test on multiple browsers (Chrome, Firefox, Safari, Edge)
10. Test with various query lengths and content types
11. Verify CORS works correctly (if applicable)

## 9. File Structure & Organization
### New Files
*No new files required - all changes will be made to existing `index.html`*

### Modified Files
- `scripts/coding_agents/index.html`
  - Modify `sendMessage()` function to call REST API
  - Add async/await implementation
  - Add error handling logic
  - Add loading state management
  - Update message display to show API responses

### API Documentation
- `scripts/coding_agents/ai_docs/templates/api_description.md` - Reference for API usage

### Notes
- API endpoint: `https://gollnickdatarag.azurewebsites.net/api/rag`
- Query parameter: `query` (must be URL-encoded)
- Response format: `{"answer": "response text"}`
- Use `encodeURIComponent()` for proper URL encoding
- Consider adding a simple loading message like "Thinking..." while waiting for API response
- Error messages should be user-friendly (e.g., "Sorry, I couldn't process your request. Please try again.")
- Maintain existing chat UI styling and structure
- Ensure API calls don't interfere with modal open/close functionality

