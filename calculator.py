{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMnpo5tHrWwdAWOfzEUtdR6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ayesha-svg/app.py/blob/main/calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B-qGwVpUBxKC",
        "outputId": "0dca177b-66a0-401e-be03-c0588f7c4aff"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a mathematical expression (use math functions like sqrt, sin, cos, etc.): 1\n",
            "Result: 1\n"
          ]
        }
      ],
      "source": [
        "# Importing necessary libraries\n",
        "import math\n",
        "\n",
        "def calculate(expression):\n",
        "    try:\n",
        "        # Evaluating the expression\n",
        "        result = eval(expression, {\"__builtins__\": None}, math.__dict__)\n",
        "        return result\n",
        "    except Exception as e:\n",
        "        return str(e)\n",
        "\n",
        "# Taking user input\n",
        "expression = input(\"Enter a mathematical expression (use math functions like sqrt, sin, cos, etc.): \")\n",
        "result = calculate(expression)\n",
        "print(\"Result:\", result)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "def calculate(expression):\n",
        "    try:\n",
        "        # Evaluating the expression\n",
        "        result = eval(expression, {\"__builtins__\": None}, math.__dict__)\n",
        "        return result\n",
        "    except Exception as e:\n",
        "        return str(e)\n",
        "\n",
        "# Taking user input\n",
        "expression = input(\"Enter a mathematical expression (use math functions like sqrt, sin, cos, etc.): \")\n",
        "result = calculate(expression)\n",
        "print(\"Result:\", result)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W4nyMKbXCh0P",
        "outputId": "2153d2f3-2e01-449f-ed44-71728ce3b6e5"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a mathematical expression (use math functions like sqrt, sin, cos, etc.): sqrt(25)\n",
            "Result: 5.0\n"
          ]
        }
      ]
    }
  ]
}