package org.example;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

/**
 * Аннотация {@code AutoInjectable} используется для обозначения классов или полей,
 * которые должны быть автоматически инъектированы с использованием механизма
 * рефлексии. Эта аннотация позволяет указать путь к файлу конфигурации,
 * содержащему информацию о зависимостях, которые нужно инъектировать.
 *
 * <p>Аннотация имеет одну опциональную строковую переменную {@code filepath},
 * которая по умолчанию указывает на "reflection/src/main/resources/injectable.properties".
 * Этот файл может содержать настройки для инъекции зависимостей.</p>
 *
 * <p>Аннотация доступна во время выполнения благодаря политике хранения
 * {@link RetentionPolicy#RUNTIME}.</p>
 *
 * @see Retention
 * @see RetentionPolicy
 */
@Retention(RetentionPolicy.RUNTIME)
public @interface AutoInjectable {
    /**
     * Путь к файлу конфигурации, содержащему информацию о зависимостях для инъекции.
     *
     * @return путь к файлу конфигурации, по умолчанию "reflection/src/main/resources/injectable.properties"
     */
    String filepath() default "reflection/src/main/resources/injectable.properties";
}
