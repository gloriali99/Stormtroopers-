let rules_data = [
    {
        "id" : 0,
        "name": "The first rule is the best rule",
        "tree": {
            "AND":  
            [
                {
                    "rule": "length",
                    "comparator": ">=",
                    "value": "2"
                },
                {
                    "OR":
                    [
                        {
                            "rule": "avgSeverity",
                            "comparator": ">=",
                            "value": "0.6"
                        },
                        {
                            "rule": "maxSeverity",
                            "comparator": ">=",
                            "value": "0.9"
                        },
                        {
                            "rule": "length",
                            "comparator": "<=",
                            "value": "-5"
                            
                        }
                    ]
                }
            ]
        },
        "to": ["to1@gmail.com", "to2@outlook.com"],
        "cc": [],
        "bcc": []
    },
    {
        "id" : 1,
        "name": "I AM NUMBER TWO",
        "tree": {
            "OR":
            [
                {
                    "rule": "length",
                    "comparator": "<=",
                    "value": "2"
                },
                {
                    "rule": "length",
                    "comparator": ">=",
                    "value": "8"
                }
            ]
        },
        "to": ["abc@gmail.com"],
        "cc": ["tothecc@cc.com"],
        "bcc": []
    },
    {
        "id" : 2,
        "name": "I AM NUMBER THREE",
        "tree": {
            "rule": "cluster",
            "comparator": "==",
            "value": "2" 
        },
        "to": ["abc@gmail.com"],
        "cc": [],
        "bcc": ["bcc@gmail.com"]
    }
]