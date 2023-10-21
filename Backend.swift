import Foundation
import OpenAISwift
import SwiftUI

func getChatbotResponse(_ inputText: String) -> String {
    let openAIClient = OpenAIClient(apiKey: "YOUR_OPENAI_API_KEY")
    let prompt = Prompt(engine: .davinci, options: Prompt.Options(maxTokens: 150, temperature: 0.7, prompt: inputText))
    let chatbotResponse = openAIClient.complete(prompt: prompt)
    return chatbotResponse.choices[0].text.strip()
}

struct ContentView: View {
    @State private var userInput = ""
    @State private var chatLog = ""

    var body: some View {
        VStack {
            Text(chatLog)
                .padding()

            TextField("Enter your text here", text: $userInput)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Button(action: showChatbotResponse) {
                Text("Send")
            }
        }
    }

    func showChatbotResponse() {
        if userInput.lowercased() == "exit" || userInput.lowercased() == "quit" || userInput.lowercased() == "bye" {
            chatLog += "Chatbot: Goodbye!\n"
            return
        }
        chatLog += "You: " + userInput + "\n"
        let chatbotResponse = getChatbotResponse(userInput)
        chatLog += "Chatbot: " + chatbotResponse + "\n"
        userInput = ""
    }
}
