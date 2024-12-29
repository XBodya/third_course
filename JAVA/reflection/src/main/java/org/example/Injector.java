package org.example;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Properties;

/**
 * Класс {@code Injector} предоставляет функциональность для инъекции зависимостей
 * в объекты с использованием механизма рефлексии. Он ищет поля, помеченные аннотацией
 * {@link AutoInjectable}, и заполняет их значениями, указанными в конфигурационных
 * файлах свойств.
 *
 * <p>Класс поддерживает инъекцию полей, но методы инъекции закомментированы и могут
 * быть активированы при необходимости.</p>
 */
public class Injector {

    /**
     * Выполняет инъекцию зависимостей в заданный объект.
     *
     * <p>Метод ищет все поля в объекте, помеченные аннотацией {@link AutoInjectable},
     * и загружает соответствующие значения из конфигурационных файлов свойств.
     * Если путь к файлу не существует или возникает ошибка при загрузке свойств,
     * будет выброшено {@link RuntimeException}.</p>
     *
     * @param obj объект, в который будут инъектированы зависимости
     * @return объект с инъектированными зависимостями
     * @throws FileNotFoundException если файл свойств не найден
     */
    static public Object inject(Object obj) throws FileNotFoundException {
        // prepare prop methods in hashmap for injectable files
        HashMap<String, ArrayList<Field>> tableInjectableFields = new HashMap<>();
        // HashMap<String, ArrayList<Method>> tableInjectableMethods = new HashMap<>();

        // Сбор полей для инъекции
        for(Field field : obj.getClass().getDeclaredFields()){
            if(isInjectable(field)){
                AutoInjectable currentAnnotate = field.getAnnotation(AutoInjectable.class);
                if(!tableInjectableFields.containsKey(currentAnnotate.filepath()))
                    tableInjectableFields.put(currentAnnotate.filepath(), new ArrayList<>());
                tableInjectableFields.get(currentAnnotate.filepath()).add(field);
            }
        }

        // Вывод полей для инъекции
        System.out.println("Fields:");
        for(String propFilepath: tableInjectableFields.keySet()){
            System.out.print(propFilepath + ": ");
            for(Field curF: tableInjectableFields.get(propFilepath)){
                System.out.print(curF.getName() + " ");
            }
            System.out.println();
        }
        System.out.println();

        // Загрузка свойств и инъекция значений в поля
        for(String propFilepath: tableInjectableFields.keySet()){
            Properties curProp = new Properties();
            File fileProp = new File(propFilepath);
            FileReader readerProp = new FileReader(fileProp);
            try {
                curProp.load(readerProp);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            for(Field curF: tableInjectableFields.get(propFilepath)){
                try {
                    if(curProp.get(getFullNameField(curF)) != null)
                        curF.set(obj, curProp.get(getFullNameField(curF)));
                } catch (IllegalAccessException e) {
                    throw new RuntimeException(e);
                }
            }
        }

        return obj;
    }

    /**
     * Проверяет, является ли поле инъектируемым, то есть, имеет ли оно аннотацию
     * {@link AutoInjectable}.
     *
     * @param obj поле для проверки
     * @return {@code true}, если поле инъектируемое, {@code false} в противном случае
     */
    static private boolean isInjectable(Field obj){
        return obj.isAnnotationPresent(AutoInjectable.class);
    }

    /**
     * Получает полное имя поля, включая имя класса и имя поля.
     *
     * @param curF поле, для которого нужно получить полное имя
     * @return полное имя поля в формате "имя_класса.имя_поля"
     */
    static private String getFullNameField(Field curF){
        return curF.getDeclaringClass().getName() + "." + curF.getName();
    }

    // Закомментированные методы для инъекции методов могут быть добавлены позже
    // static private boolean isInjectable(Method obj){
    //     return obj.isAnnotationPresent(AutoInjectable.class);
    // }
}
