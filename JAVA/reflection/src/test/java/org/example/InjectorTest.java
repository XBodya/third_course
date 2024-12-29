package org.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Field;

import static org.junit.jupiter.api.Assertions.*;

class InjectorTest {

    private static final String TEST_PROPERTIES_FILE = "test.properties";

    @BeforeEach
    void setUp() throws IOException {
        // Создание файла свойств для тестирования
        try (FileWriter writer = new FileWriter(TEST_PROPERTIES_FILE)) {
            writer.write("org.example.TestClass.field1=value1\n");
            writer.write("org.example.TestClass.field2=value2\n");
        }
    }

    @Test
    void testInjectFields() throws Exception {
        TestClass testObject = new TestClass();
        Injector.inject(testObject);

        assertEquals("value1", testObject.field1);
        assertEquals("value2", testObject.field2);
    }

    @Test
    void testInjectFieldsWithMissingProperty() throws Exception {
        // Удаление или изменение свойства для теста
        try (FileWriter writer = new FileWriter(TEST_PROPERTIES_FILE)) {
            writer.write("org.example.TestClass.field1=value1\n");
            // field2 отсутствует
        }

        TestClass testObject = new TestClass();
        Injector.inject(testObject);

        assertEquals("value1", testObject.field1);
        assertNull(testObject.field2); // поле должно остаться null
    }

    @Test
    void testInjectNonInjectableField() throws Exception {
        NonInjectableClass testObject = new NonInjectableClass();
        Injector.inject(testObject);

        assertNull(testObject.nonInjectableField); // поле должно оставаться null
    }

    @Test
    void testFileNotFoundException() {
        // Удаляем файл свойств
        new File(TEST_PROPERTIES_FILE).delete();

        TestClass testObject = new TestClass();
        assertThrows(FileNotFoundException.class, () -> Injector.inject(testObject));
    }

    // Вспомогательные классы для тестирования
    static class TestClass {
        @AutoInjectable(filepath = TEST_PROPERTIES_FILE)
        public String field1;

        @AutoInjectable(filepath = TEST_PROPERTIES_FILE)
        public String field2;
    }

    static class NonInjectableClass {
        public String nonInjectableField;
    }
}
