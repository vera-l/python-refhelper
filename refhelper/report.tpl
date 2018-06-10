<!DOCTYPE html>
<html>
    <head>
        <title>Report {{ target_path }} | task &laquo;{{ task }}&raquo;</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <style>
            body {
                padding: 20px 30px 10px;
                font-family: 'PT Mono', monospace;
                color: #586E75;
                background-color: #FDF6E3;
                font-size: 1em;
            }
            a:link, a:visited {
                font-weight: bold;
                color: #2AA198;
                border-bottom: 1px solid #2AA198;
                text-decoration: none;
            }
            a:hover, a:active {
                color: #D33682;
                border-bottom: 1px solid #D33682;
            }
            h1 {
                margin: 0 0 30px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 30px;
            }
            th {
                text-align: left;
                font-weight: normal;
                font-style: italic;
                color: #859900;
                font-size: 0.7em;
            }
            tr td:nth-child(3), tr td:nth-child(4) {
                width: 30px;
            }
            td {
                padding: 5px 0;
            }
            .datetime {
                font-style: italic;
                font-size: 0.6em;
                color: #93A1A1;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <h1>{{ target_path }} | task &laquo;{{ task }}&raquo; ({{ len }} items)</h1>
        <table class="results">
            <thead>
                <th>
                    file
                </th>
                <th>
                    line
                </th>
                <th>
                    column
                </th>
            </thead>
            <tbody>{% for item in results %}
                <tr>
                    <td>
                        <input class="idea-opened" type="checkbox" disabled="disabled" />
                        <a class="idea-link" href="{{ idea_url }}?file={{item.file}}&line={{item.line}}&column={{item.column}}">{{ item.file }}</a>
                    </td>
                    <td>
                        {{ item.line }}
                    </td>
                    <td>
                        {{ item.column }}
                    </td>
                </tr>{% endfor %}
            </tbody>
        </table>
        <p class="datetime">{{ datetime }}. Firstly, open target project in IntelliJ idea.
            Then click by each link will open code in this IDE.</p>
        <script>
            (function(){
                let fakeImg = new Image();
                document.querySelector('.results').addEventListener('click', function(e) {
                    let current = e.target;
                    while(current) {
                         if(current.classList.contains('idea-link')) {
                            let href = current.href;
                            fakeImg.src = href;
                            current.parentNode.querySelector('.idea-opened').checked = true;
                            break;
                        };
                        if(current !== e.target) {
                            break;
                        }
                        current = current.parentNode;
                    }
                    e.preventDefault();
                })
            })();
        </script>
    </body>
</html>
