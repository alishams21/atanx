<div align="center">
  <img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=0fcbab94-8fbe-4a38-93e8-c2348450a42e" />
  <h1 align="center">Connecting AI, Software and Cloud Infrastructure seamlessly.
</h1>
</div>

<div align="center">

  <!-- PROJECT LOGO -->
  <br />
    <a href="https://zenml.io">
      <img alt="Atanx Logo" src="docs/book/.gitbook/assets/header.jpeg" alt="ZenML Logo">
    </a>
  <br />

</div>


Atanx leverages GenAI and GenUI to automate building and provisioning of data analysis and data science services easier and in self-service manner.

---
## 🤸 Quickstart

### **Step 1: Create .env and .env.local in backend folder and in frontend folder respectively with the following variables:**

```bash
OPENAI_API_KEY
```

### **Step 2: Install the Atanx via makefile**

```bash
make start-all
```
this will install the Atanx UI, Backend, Provisioner and Gateway.

### **Step 3: To stop the Atanx via makefile**

```bash
make stop-all
```
---
## 🪄 Simple, Integrated, End-to-end AI operations
#### Use benefits of stateful GenUI to chat with your datasets. States will be maintained across backend and frontend and your application fully aware of the state of the conversation.
![First step](/docs/book/.gitbook/assets/analysisstep.gif)

#### After enough exploration of data you can ask Atanx to generate a prompt based on your chat history, this prompt will be used to generate your analyzer code you can customize that based on your needs. Now you have all the information in hand to ask Atanx to generate code for you. In UI you give all the information about inputs, features, output, rules, limitation, analysis type and prompt and Atanx will generate analyzer for your.

![Second step](/docs/book/.gitbook/assets/secondstep.gif)


#### Easily provision your services stack by reusing your existing infrastructure. Have your analyzer in frontend if you prefer manual run from UI or in backend through reset service if you want to share with your organization developers and applications integration.

![Third step](/docs/book/.gitbook/assets/frontendanalyzerrun.gif)

## 🔗✨ Logical Architecture
Following is the logical architecture of Atanx.  
1- Atanx UI is a NextJS application that is used to interact with the Atanx backend through Gateway.  
2- Atanx Backend is an AI agent based Python application that is used to generate analyzer code based on info from UI.  
3- Provisioner is a Python application which is used to provision analyzers by monitoring Registry.  
4- Gateway is a Python application that is used to interact with different services routing the requests to appropriate services.  

![Logical Architecture](/docs/book/.gitbook/assets/logical.jpeg)
## ⭐ Show Your Support

If you find Atanx helpful or intriguing, we would love for you to show your appreciation by ⭐ starring us on GitHub. Your support not only helps raise the visibility of the project but also encourages others to explore its potential.

Thank you for your support! 🌟

---

## 🚀 Looking to Contribute?
We see great potential in Atanx, and we're excited for you to join us on this journey. If you're interested in contributing, feel free to connect with us and be part of the project's growth!
