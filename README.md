# streamlit_incometracker_grapher
Uses Streamlit, tabs on page, sankey graph using plotly and sqllite database

# Links
- [Build A Streamlit Web App From Scratch (incl. NoSQL Database + interactive Sankey chart)](https://youtu.be/3egaMfE9388)
- [Emoji Cheat Sheet](https://www.webfx.com/tools/emoji-cheat-sheet/)
- [Create custom Azure Templates](https://portal.azure.com/#create/Microsoft.Template)
- [YouTube Video on deploying Streamlit to Azure](https://youtu.be/2toRzAYT8yo)
- [Bootstrap Icons](https://icons.getbootstrap.com)

# Instructions
- On VDI 
    - Check streamlit : python3 -m streamlit hello
    - Run app : streamlit run app.py
- On Azure
    - Deploy to a B1 appservice webapp as it has sockets support that streamlit needs
    - You can also connect B1 to github ci/cd
    - Configuration -> General Settings -> Startup Command :
        - python -m streamlit run app.py --server.port 8000