<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>342</width>
    <height>286</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="dinheiro">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>30</y>
      <width>111</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Dinheiro (em milhões) : </string>
    </property>
   </widget>
   <widget class="QSpinBox" name="qtd_dinheiro">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>30</y>
      <width>42</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="pessoa">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>80</y>
      <width>131</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Quantidade de Pessoas :</string>
    </property>
   </widget>
   <widget class="QSpinBox" name="qtd_pessoa">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>80</y>
      <width>42</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="risco">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>160</y>
      <width>41</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Risco :</string>
    </property>
   </widget>
   <widget class="QLabel" name="resultado">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>155</y>
      <width>211</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
   </widget>
   <widget class="QPushButton" name="calcular">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>130</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Calcular</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>342</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>