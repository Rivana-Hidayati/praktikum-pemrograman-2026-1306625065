{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Rivana-Hidayati/praktikum-pemrograman-2026-1306625065/blob/main/SC_Modul_2_1306625065.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KlTDrBOB4S5N",
        "outputId": "8ea1c17f-c1f0-4274-fa72-e3cff3d96d9e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Program Faktor Bilangan\n",
            "Nama : Rivana hidayati\n",
            "NIM : 1306625065\n",
            "\n",
            "masukkan bilangan < 100 (masukkan 0 untuk selesai) = 13\n",
            "masukkan bilangan < 100 (masukkan 0 untuk selesai) = 14\n",
            "Bilangan 13 -> faktornya = [1, 13]\n",
            "Bilangan 14 -> faktornya = [1, 2, 7, 14]\n",
            "Bilangan 13 dan 14 -> faktor yang sama =\n",
            "\n",
            "masukkan bilangan < 100 (masukkan 0 untuk selesai) = 18\n",
            "masukkan bilangan < 100 (masukkan 0 untuk selesai) = 30\n",
            "Bilangan 18 -> faktornya = [1, 2, 3, 6, 9, 18]\n",
            "Bilangan 30 -> faktornya = [1, 2, 3, 5, 6, 10, 15, 30]\n",
            "Bilangan 18 dan 30 -> faktor yang sama =\n",
            "\n",
            "masukkan bilangan < 100 (masukkan 0 untuk selesai) = 0\n",
            "masukkan bilangan < 100 (masukkan 0 untuk selesai) = 0\n",
            "Program Selesai\n"
          ]
        }
      ],
      "source": [
        "print(\"Program Faktor Bilangan\")\n",
        "print(\"Nama : Rivana hidayati\")\n",
        "print(\"NIM : 1306625065\")\n",
        "print()\n",
        "\n",
        "while True :\n",
        "  a = int(input(\"masukkan bilangan < 100 (masukkan 0 untuk selesai) = \"))\n",
        "  b = int(input(\"masukkan bilangan < 100 (masukkan 0 untuk selesai) = \"))\n",
        "\n",
        "  hasil_a = []\n",
        "  hasil_b = []\n",
        "\n",
        "  if a >= 100 or b >= 100:\n",
        "    print(\"Error\")\n",
        "    break\n",
        "\n",
        "  elif a == 0 and b == 0 :\n",
        "    print (\"Program Selesai\")\n",
        "    break\n",
        "\n",
        "  for i in range(1, a+1):\n",
        "    if a % i == 0:\n",
        "      hasil_a.append(i)\n",
        "\n",
        "  for i in range(1, b+1):\n",
        "    if b % i == 0:\n",
        "      hasil_b.append(i)\n",
        "\n",
        "    hasil_sama = []\n",
        "\n",
        "    for i in hasil_a:\n",
        "      if i in hasil_b:\n",
        "        hasil_sama.append(i)\n",
        "\n",
        "  print(\"Bilangan\", a, \"-> faktornya =\", hasil_a)\n",
        "  print(\"Bilangan\", b, \"-> faktornya =\", hasil_b)\n",
        "  print(\"Bilangan\", a, \"dan\", b, \"-> faktor yang sama =\")\n",
        "\n",
        "  print()"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP9DcU/QX/SAyMc/sttpuHW",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}