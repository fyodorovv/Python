import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

import strings as st


def isWin(arr, who):  # проверка на выигрыш
    if (((arr[0] == who) and (arr[4] == who) and (arr[8] == who)) or
            ((arr[2] == who) and (arr[4] == who) and (arr[6] == who)) or
            ((arr[0] == who) and (arr[1] == who) and (arr[2] == who)) or
            ((arr[3] == who) and (arr[4] == who) and (arr[5] == who)) or
            ((arr[6] == who) and (arr[7] == who) and (arr[8] == who)) or
            ((arr[0] == who) and (arr[3] == who) and (arr[6] == who)) or
            ((arr[1] == who) and (arr[4] == who) and (arr[7] == who)) or
            ((arr[2] == who) and (arr[5] == who) and (arr[8] == who))):
        return True
    return False


# cellArray - массив данных из callBackData, полученных после нажатия на callBack-кнопку
def countUndefinedCells(cellArray):
    counter = 0
    for i in cellArray:
        if i == st.SYMBOL_UNDEF:
            counter += 1
    # возвращает количество неопределенных ячеек (т.е. количество ячеек, в которые можно сходить)
    return counter


# callBackData - данные для формирования callBack данных обновленного игрового поля
def game(callBackData):  # проверка возможности хода крестиком, проверка победы крестика, ход бота (ноликом), проверка победы ботом
    message = st.ANSW_YOUR_TURN  # сообщение, которое вернется
    alert = None

    # считывание нажатой кнопки, преобразуя ее из строки в число
    buttonNumber = int(callBackData[0])
    if not buttonNumber == 9:  # цифра 9 передается в первый раз в качестве заглушки.
        # строчка callBackData разбивается на посимвольный список ['1', '2', '3']
        charList = list(callBackData)
        # удаление из списка первого элемента: который отвечает за выбор кнопки
        charList.pop(0)
        # проверка: если в нажатой кнопке не выбран крестик/нолик, то можно туда сходить крестику
        if charList[buttonNumber] == st.SYMBOL_UNDEF:
            charList[buttonNumber] = st.SYMBOL_X  # эмуляция хода крестика
            if isWin(charList, st.SYMBOL_X):  # проверка: выиграл ли крестик после своего хода
                message = st.ANSW_YOU_WIN
            else:  # если крестик не выиграл, то может сходит бот, т.е. нолик
                # проверка: есть ли свободные ячейки для хода
                if countUndefinedCells(charList) != 0:
                    # если есть, то ходит бот (нолик)
                    isCycleContinue = True
                    # запуск бесконечного цикла т.к. необходимо, чтобы бот походил в свободную клетку, а клетка выбирается случайным образом
                    while (isCycleContinue):
                        # генерация случайного числа - клетки, в которую сходит бот
                        rand = random.randint(0, 8)
                        # если клетка неопределенна, то ходит бот
                        if charList[rand] == st.SYMBOL_UNDEF:
                            charList[rand] = st.SYMBOL_O
                            isCycleContinue = False  # смена значения переменной для остановки цикла
                            # проверка: выиграл ли бот после своего кода
                            if isWin(charList, st.SYMBOL_O):
                                message = st.ANSW_BOT_WIN

        # если клетка, в которую хотел походить пользователь уже занята:
        else:
            alert = st.ALERT_CANNOT_MOVE_TO_THIS_CELL

        # проверка: остались ли свободные ячейки для хода и что изначальное сообщение не поменялось (означает, что победителя нет, и что это был не ошибочный ход)
        if countUndefinedCells(charList) == 0 and message == st.ANSW_YOUR_TURN:
            message = st.ANSW_DRAW

        # формирование новой строчки callBackData на основе сделанного хода
        callBackData = ''
        for c in charList:
            callBackData += c

    # проверка, что игра закончилась (message равно одному из трех вариантов: победил Х, 0 или ничья):
    if message == st.ANSW_YOU_WIN or message == st.ANSW_BOT_WIN or message == st.ANSW_DRAW:
        message += '\n'
        for i in range(0, 3):
            message += '\n | '
            for j in range(0, 3):
                message += callBackData[j + i * 3] + ' | '
        callBackData = None  # обнуление callBackData

    return message, callBackData, alert


# возвращает клавиатуру для бота
def getKeyboard(callBackData):  # на вход получает callBackData - данные с callBack-кнопки

    keyboard = [[], [], []]  # заготовка объекта клавиатуры, которая вернется

    if callBackData != None:
        # формирование объекта клавиатуры
        for i in range(0, 3):
            for j in range(0, 3):
                keyboard[i].append(InlineKeyboardButton(
                    callBackData[j + i * 3], callback_data=str(j + i * 3) + callBackData))

    return keyboard


def newGame(update, _):
    # сформировать callBack данные для первой игры, то есть строку, состояющую из 9 неопределенных символов
    data = ''
    for i in range(0, 9):
        data += st.SYMBOL_UNDEF

    # отправить сообщение для начала игры
    update.message.reply_text(
        st.ANSW_YOUR_TURN, reply_markup=InlineKeyboardMarkup(getKeyboard(data)))


def button(update, _):
    query = update.callback_query
    callbackData = query.data  # получение callbackData, скрытых в кнопке

    message, callbackData, alert = game(callbackData)  # игра
    # если не получен сигнал тревоги (alert==None), то редактируем сообщение и меняем клавиатуру
    if alert is None:
        query.answer()  # обязательно нужно что-то отправить в ответ, иначе могут возникнуть проблемы с ботом
        query.edit_message_text(
            text=message, reply_markup=InlineKeyboardMarkup(getKeyboard(callbackData)))
    # если получен сигнал тревоги (alert!=None), то отобразить сообщение о тревоге
    else:
        query.answer(text=alert, show_alert=True)


if __name__ == '__main__':
    updater = Updater("5721607031:AAGVO7c9RisGqP-sBkVCQASbJ3TSwixg-jQ")

    # добавление обработчиков
    updater.dispatcher.add_handler(CommandHandler('start', newGame))
    updater.dispatcher.add_handler(CommandHandler('new_game', newGame))
    # добавление обработчика на CallBack кнопки
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    updater.start_polling()
    updater.idle()
