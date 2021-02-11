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
            table a {
                font-weight: bold;
            }
            th {
                text-align: left;
                font-weight: normal;
                color: #859900;
                font-size: 0.7em;
                padding-bottom: 15px;
            }
            tr td:nth-child(3), tr td:nth-child(4) {
                width: 30px;
            }
            td {
                padding: 5px 0;
            }
            tr:hover td {
                background: rgba(0, 0, 0, 0.05);
            }
            .datetime {
                font-style: italic;
                font-size: 0.6em;
                color: #93A1A1;
                margin: 0;
            }
            .datetime a:link, .datetime a:visited {
                color: #93A1A1;
                border-bottom: 1px solid #e1e1e1;
            }
            .datetime a:hover, .datetime a:active {
                border: 0;
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
        <p class="datetime">
            {{ datetime }}.
            <a href="https://github.com/vera-l/python-refhelper">pyrefhelper</a> v{{ version }}.
            Firstly, open target project with IntelliJ Idea.
            After that you can open target code by click on links.
        </p>
        <script>
            (function(){
                document.querySelector('.results').addEventListener('click', function(e) {
                    const current = e.target.closest('.idea-link');
                    if (current) {
                        fetch(current.href).then(function () {
                            current.parentNode.querySelector('.idea-opened').checked = true;
                        });
                    };
                    e.preventDefault();
                })
            })();
        </script>
    </body>
</html>
