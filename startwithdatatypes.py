{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPBgJ6hEv+p7i5hqS8BGY7D",
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
        "<a href=\"https://colab.research.google.com/github/Garima-2702/Garima-2702/blob/Basic-of-python/Untitled0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "A7bqw3c_nv--"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rNMJsvxVk1jp",
        "outputId": "f9a12154-69a0-41e2-f3f8-94a21d22fe33"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter first number20\n",
            "enter second number10\n",
            "30\n"
          ]
        }
      ],
      "source": [
        "a=input('enter first number')\n",
        "b=input('enter second number')\n",
        "c=int(a)+int(b)\n",
        "print(c)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=input('enter first number')\n",
        "b=input('enter second number')\n",
        "float(c)==float(a)+float(b)\n",
        "print(c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X2ykXGtsn2e1",
        "outputId": "9cf00560-fa09-455d-cfea-137c2eb05543"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter first number20\n",
            "enter second number10\n",
            "7.199999999999999\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=input('enter a number')\n",
        "print(type(a))\n",
        "\n",
        "print(type(int(a)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LoHfBf-0pH5G",
        "outputId": "d32b4945-84e4-4286-c2cd-8b1b27d005f9"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a number20\n",
            "<class 'str'>\n",
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=input('enter a number')\n",
        "print(bool(a))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dckQaXlPqcoj",
        "outputId": "29c26c18-a511-484a-b252-0417c6e1b992"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a number-2\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=input('enter first number')\n",
        "b=input('enter second number')\n",
        "c=int(a)+int(b)\n",
        "print(\"addition =\")\n",
        "print(c)\n",
        "d=int(a)-int(b)\n",
        "print(\"subtraction =\")\n",
        "print(d)\n",
        "e=int(a)*int(b)\n",
        "print(\"multiplication =\")\n",
        "print(e)\n",
        "f=int(a)/int(b)\n",
        "print(\"division\")\n",
        "print(f)\n",
        "g=int(a)%int(b)\n",
        "print(\"modulous =\")\n",
        "print(g)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vf_1Q7AUrT3M",
        "outputId": "04b88f76-9240-4f3f-edb0-4af711d3be36"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter first number4\n",
            "enter second number2\n",
            "addition =\n",
            "6\n",
            "subtraction =\n",
            "2\n",
            "multiplication =\n",
            "8\n",
            "division\n",
            "2.0\n",
            "modulous =\n",
            "0\n"
          ]
        }
      ]
    }
  ]
}
